import requests
from twilio.rest import Client
import config

weather_endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
api_key = config.WEATHER_API_KEY
account_sid = 'AC17f93b05c4da00e15840b6c447e834ae'
auth_token = config.AUTH_TOKEN

weather_params = {
    "lat": 54.687157,
    "lon": 25.279652,
    "appid": api_key,
    "units": 'metric',
    "cnt": 4
}

response = requests.get(weather_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        rain = True
if rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+13308596536',
        body='It will rain today',
        to='+37067727815'
    )
    print(message.status)
else:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+13308596536',
        body='It will not rain today',
        to='+37067727815'
    )
    print(message.status)
