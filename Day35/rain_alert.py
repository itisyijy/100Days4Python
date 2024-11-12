# Day35 for 100Days4Python
# Day35 : API Keys, Authentication, Environment Variables and Sending SMS
# Project for Day35 : Rain Alert

import os
import requests
from twilio.rest import Client

from_phone_num = "whatsapp:+{TWILIO_PHONE_NUMBER}"
to_phone_num = "whatsapp:+{VERIFIED_PHONE_NUMBER}"
account_sid = "ACCOUNT_SID"
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

API_KEY = os.environ.get("OPEN_WEATHER_MAP_API")
lat = "37.532600"
lon = "127.024612"

open_weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": API_KEY,
}
open_weather = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",
                            params=open_weather_params)
open_weather.raise_for_status()
weather_data = open_weather.json()

weather_code_12hours = []
need_umbrella = False
for next_3hours in weather_data["list"][:40]:    # slicing!
    weather_code_12hours.append(next_3hours["weather"][0]["id"])
    if int(weather_code_12hours[-1]) < 700:
        need_umbrella = True
print(weather_code_12hours)

if need_umbrella:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Bring an your Umbrella.",
        from_=from_phone_num,
        to=to_phone_num,
    )
    print(message.sid)
