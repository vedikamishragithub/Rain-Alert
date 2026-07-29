
import os
import requests

api_key = os.environ["OWM_API_KEY"]

lat = 18.5204
lon = 73.8567

url_weather = "https://api.openweathermap.org/data/2.5/forecast"

params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url_weather, params=params)
response.raise_for_status()
weather_data = response.json()

message = "✅ Hello from GitHub Actions!"

for forecast in weather_data["list"]:
    weather = forecast["weather"][0]["id"]

    if 200 <= weather < 600:
        message = "Bring an umbrella ☔"
        break

if message:
    TOKEN = os.environ["BOT_TOKEN"]
    CHAT_ID = os.environ["CHAT_ID"]

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": message
        }
    )
