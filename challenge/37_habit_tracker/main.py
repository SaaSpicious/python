from datetime import datetime
import requests

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "dasdennis87"
TOKEN = "" #Set a token of your choice!
GRAPH_ID = "firstgraph"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

headers = {
    "X-USER-TOKEN": TOKEN,
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "workout Graph",
    "unit": "kg",
    "type": "int",
    "color": "shibafu"
}

# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
today_string = datetime.now().strftime("%Y%m%d")

pixel_config = {
    "date": today_string,
    "quantity": "1"
}

response = requests.post(url=pixel_endpoint,json=pixel_config,headers=headers)
print(response.text)