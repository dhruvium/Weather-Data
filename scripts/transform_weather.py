import json
import csv
import os

with open("data/raw/weather_raw.json", "r") as f:
    data = json.load(f)

hourly = data["hourly"]
times = hourly["time"]
temps = hourly["temperature_2m"]
winds = hourly["wind_speed_10m"]

os.makedirs("data/processed", exist_ok=True)

with open("data/processed/weather_clean.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["time", "temperature_2m", "wind_speed_10m"])

    for i in range(len(times)):
        writer.writerow([times[i], temps[i], winds[i]])

print("Clean CSV saved.")
