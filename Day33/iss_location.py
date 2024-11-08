# Day33 for 100Days4Python
# Day33 : Application Programming Interface, API

import requests

# Get data from API endpoint
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status() # Raise exception according to API response code
print(response) # <Response [200]> -> response code!

data = response.json()  # Get data as .json file
print(data)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)
print(iss_position)
