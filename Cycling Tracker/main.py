import requests
from datetime import datetime


USERNAME = "your user name"
TOKEN = "your password"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_param = {
    "token": TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_param1 = {
    "id": GRAPH_ID,
    "name" : "cycling graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "momiji",
}

headers ={
    "X-USER-TOKEN": TOKEN
}

today = datetime.now()

post_params = {
    "date" : today.strftime("%Y%m%d"),
    "quantity"  : input("how many km did you cycle today? "),
}



post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

response = requests.post(url=post_endpoint, json=post_params, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

put_params = {
    "quantity" : "10"
}

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
