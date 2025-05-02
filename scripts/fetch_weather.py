import requests
import yaml
import time
from datetime import datetime, timezone  # Add timezone import

# Load configuration
with open("E:/Project_Environments/weather_dashboard/configs/config.yaml", "r") as file:
    config = yaml.safe_load(file)
API_KEY = config["openweathermap"]["api_key"]
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city="London"):
    """
    Fetch weather data for a given city from OpenWeatherMap API.
    Args:
        city (str): City name (default: London)
    Returns:
        dict: Weather data or None if the request fails
    """
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()
        weather_data = {
            "city": city,
            "timestamp": datetime.now(timezone.utc).isoformat(),  # Fixed line
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"]
        }
        return weather_data
    except requests.RequestException as e:
        print(f"Error fetching data for {city}: {e}")
        return None

if __name__ == "__main__":
    weather = fetch_weather("London")
    if weather:
        print(weather)