# Day38 for 100Days4Python
# Day38 : Exercise Tracking with Python and Google Sheets

import os
import requests
from _datetime import datetime

NUTRITIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
NUTRITIONIX_APP_KEY = os.environ.get("NUTRITIONIX_APP_KEY")

nutritionix_headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_APP_KEY,
}

SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}",
}

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutritionix_query = input("Today's Workout Briefing >>> ")
nutritionix_config = {
    "query": nutritionix_query,
    "weight_kg": "67",
    "height_cm": "172",
    "age": "23",
}
nutritionix_response = requests.post(url=nutritionix_endpoint, headers=nutritionix_headers, json=nutritionix_config)
print(nutritionix_response.text)

today = datetime.now()
sheety_endpoint = "https://api.sheety.co/728913e4535b162f49b906255d80dd6c/myWorkouts/workouts"
row_config = {
    "workout": {
        "date": today.strftime("%d/%m/%Y"),
        "time": today.strftime("%x %X"),
        "exercise": nutritionix_response.json()["exercises"][0]["name"].title(),
        "duration": nutritionix_response.json()["exercises"][0]["duration_min"],
        "calories": nutritionix_response.json()["exercises"][0]["nf_calories"],
    }
}
sheety_response = requests.post(url=sheety_endpoint, headers=sheety_headers, json=row_config)
print(sheety_response.text)
