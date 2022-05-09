# Personal details have been omitted.

from datetime import datetime
import requests

USERNAME = ""
TOKEN = ""

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.json())

# Graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Pixels
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"
today = datetime(year=2022, month=4, day=15)
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "3",
}
# response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# put request
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "5",
}
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# delete request
# delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)