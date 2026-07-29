

api_key = "1fe72837a455c7c6a09ded68f8273384"


lat = 18.5204
lon = 73.8567


url_weather = "https://api.openweathermap.org/data/2.5/forecast"


params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url_weather , params=params)
weather_data=response.json()

message=" "

for i in range(4):
   weather = weather_data["list"][i]['weather'][0]['id']
   if weather >700:
       message="Bring an umbrella ☔"
       break





TOKEN = "8669144790:AAEbZd3L_wSneH-umynRm5EA4FVG331AUY4"
CHAT_ID = "8853731200"



url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

requests.post(url, data={
    "chat_id": CHAT_ID,
    "text": message
})
