# Day33 for 100Days4Python
# Day33 : Application Programming Interface, API

import time
import smtplib
import requests
from datetime import datetime

SEOUL_LAT = 37.532600
SEOUL_LNG = 127.024612


def iss_coordinate():
    # Get data from API endpoint
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()  # Raise exception according to API response code
    print(iss_response)  # <Response [200]> -> response code!
    
    iss_data = iss_response.json()  # Get data as .json file
    iss_lat = float(iss_data["iss_position"]["latitude"])
    iss_lng = float(iss_data["iss_position"]["longitude"])
    
    return (SEOUL_LAT - 5 <= iss_lat <= SEOUL_LAT + 5) and (SEOUL_LNG - 5 <= iss_lng <= SEOUL_LNG + 5)


def sunrise_sunset():
    sun_params = {
        "lat": SEOUL_LAT,
        "lng": SEOUL_LNG,
        "formatted": 0,
        "tzid": "Asia/Seoul",
    }
    sun_response = requests.get(url="https://api.sunrise-sunset.org/json", params=sun_params)
    sun_response.raise_for_status()
    sun_data = sun_response.json()
    sunrise_h = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_h = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])
    
    current_time = datetime.now()
    current_h = current_time.hour
    
    return not (sunrise_h <= current_h <= sunset_h)


while True:
    if iss_coordinate() and sunrise_sunset():
        with smtplib.SMTP("smtp.gmail.com") as gmail:
            gmail.starttls()
            gmail.login(user="itisyijy@gmail.com", password=input("PASSWORD: "))
            gmail.sendmail(from_addr="itisyijy@gmail.com", to_addrs="graycona@yahoo.com",
                           msg="Subject:Look Up In The Sky!\n\nISS is overhead of you.")
            break
    print("Please Wait.")
    time.sleep(60)
