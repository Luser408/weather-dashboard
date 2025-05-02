import boto3
import pandas as pd
import json
import configparser

# Load AWS credentials from the custom file
cred_config = configparser.ConfigParser()
cred_config.read('configs/aws_credentials')
aws_access_key_id = cred_config['default']['aws_access_key_id']
aws_secret_access_key = cred_config['default']['aws_secret_access_key']

# Initialize S3 client with the credentials
s3_client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

bucket = 'weather-data-luser403-2025'
prefix = 'raw/'

# List objects in S3
response = s3_client.list_objects_v2(Bucket=bucket, Prefix=prefix)
weather_data = []

# Read each file
for obj in response.get('Contents', []):
    s3_key = obj['Key']
    file_obj = s3_client.get_object(Bucket=bucket, Key=s3_key)
    data = json.loads(file_obj['Body'].read().decode('utf-8'))
    weather_data.append(data)

# Convert to DataFrame
df = pd.DataFrame(weather_data)
print(df.head())  # Inspect the data
df.to_csv('processed_weather_data.csv', index=False)  # Save as CSV