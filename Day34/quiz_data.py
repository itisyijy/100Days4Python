# Day34 for 100Days4Python
# Project for Day34 : Trivia Quizzler Based on Day 17

import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]
