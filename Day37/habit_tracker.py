# Day37 for 100Days4Python
# Day37 : Advanced Authentication and POST / PUT / DELETE Requests

from datetime import datetime
import requests

USERNAME = "auxigen"
TOKEN = "TOKEN"
GRAPH_ID = "exercise"

pixela_endpoint = "https://pixe.la/v1/users"
pixela_headers = {
    "X-USER-TOKEN": TOKEN,
}


# Create user
def create_user():
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    account_response = requests.post(url=pixela_endpoint, json=user_params)
    print(account_response.text)


# Create a graph
def create_graph():
    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
    graph_config = {
        "id": GRAPH_ID,
        "name": "Daily Exercise Graph",
        "unit": "minute",
        "type": "int",
        "color": "sora",
    }
    graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=pixela_headers)
    print(graph_response.text)


# Record pixel
def record_pixel():
    today = datetime.now()
    record = input("How many minutes did you exercise today? >>> ")
    record_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
    record_config = {
        "date": f"{today.strftime("%Y%m%d")}",
        "quantity": record,
    }
    record_response = requests.post(url=record_endpoint, json=record_config, headers=pixela_headers)
    print(record_response.text)


# Update pixel
def update_pixel():
    update_date = input("Enter the date to modify (yyyyMMdd) >>> ")
    update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{update_date}"
    update_config = {
        "quantity": "40",
    }
    update_response = requests.put(url=update_endpoint, json=update_config, headers=pixela_headers)
    print(update_response.text)


# Delete pixel
def delete_pixel():
    delete_date = input("Enter the date to delete (yyyyMMdd) >>> ")
    delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{delete_date}"
    delete_response = requests.delete(url=delete_endpoint, headers=pixela_headers)
    print(delete_response.text)


while True:
    print("(0) Exit\n"
          "(1) Create New User\n"
          "(2) Create New Graph\n"
          "(3) Record Today's Exercise\n"
          "(4) Update Record\n"
          "(5) Delete Record\n")
    option = input("Choose the option. >>> ")
    if option == "0":
        break
    elif option == "1":
        create_user()
    elif option == "2":
        create_graph()
    elif option == "3":
        record_pixel()
    elif option == "4":
        update_pixel()
    elif option == "5":
        delete_pixel()
    else:
        print("Check your input")
