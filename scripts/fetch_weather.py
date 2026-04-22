import requests
import json
import os

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 38.72,
    "longitude": -9.14,
    "hourly": "temperature_2m,wind_speed_10m",
    "forecast_days": 1
}

response = requests.get(url, params=params)
data = response.json()

os.makedirs("data/raw", exist_ok=True)

with open("data/raw/weather_raw.json", "w") as f:
    json.dump(data, f, indent=4)

print("Raw weather data saved.")