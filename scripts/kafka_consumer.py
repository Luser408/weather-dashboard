import json
import yaml
import boto3
import configparser
from kafka import KafkaConsumer
from datetime import datetime

# Load configuration
with open("E:/Project_Environments/weather_dashboard/configs/config.yaml", "r") as file:
    config = yaml.safe_load(file)
BOOTSTRAP_SERVERS = config["kafka"]["bootstrap_servers"]
TOPIC = config["kafka"]["topic"]
S3_BUCKET = config["aws"]["s3_bucket"]

# Read AWS credentials
cred_config = configparser.ConfigParser()
cred_config.read('E:/Project_Environments/weather_dashboard/configs/aws_credentials')
aws_access_key_id = cred_config['default']['aws_access_key_id']
aws_secret_access_key = cred_config['default']['aws_secret_access_key']

# Initialize Kafka consumer
consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=BOOTSTRAP_SERVERS,
    auto_offset_reset='latest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Initialize S3 client with credentials
s3_client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

def consume_weather_data():
    """
    Consume weather data from Kafka and store it in S3.
    """
    print("Consuming weather data from Kafka...")
    for message in consumer:
        weather_data = message.value
        timestamp = weather_data["timestamp"].replace(":", "-")  # Make S3 key safe
        s3_key = f"raw/weather_{weather_data['city']}_{timestamp}.json"
        s3_client.put_object(
            Bucket=S3_BUCKET,
            Key=s3_key,
            Body=json.dumps(weather_data)
        )
        print(f"Stored data in S3: {s3_key}")

if __name__ == "__main__":
    consume_weather_data()