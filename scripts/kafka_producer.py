import json
import time
import yaml
from kafka import KafkaProducer
from fetch_weather import fetch_weather

# Load configuration
with open("E:/Project_Environments/weather_dashboard/configs/config.yaml", "r") as file:
    config = yaml.safe_load(file)
BOOTSTRAP_SERVERS = config["kafka"]["bootstrap_servers"]
TOPIC = config["kafka"]["topic"]

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers=BOOTSTRAP_SERVERS,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def produce_weather_data(cities, interval=60):
    """
    Fetch weather data for a list of cities and send it to Kafka topic.
    Args:
        cities (list): List of city names
        interval (int): Seconds between fetches (default: 60)
    """
    while True:
        for city in cities:
            weather_data = fetch_weather(city)
            if weather_data:
                producer.send(TOPIC, weather_data)
                print(f"Sent data to Kafka: {weather_data}")
        time.sleep(interval)

if __name__ == "__main__":
    # List of 10 cities
    cities = [
    "London", "New York", "Tokyo", "Sydney", "Paris",
    "Mumbai", "Cape Town", "Toronto", "Beijing", "Rio de Janeiro", "Berlin"
    ]
    produce_weather_data(cities, 60)