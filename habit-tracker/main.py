import requests
from datetime import datetime as dt

USERNAME = "alegradi"
TOKEN = "secret"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Programming Graph",
    "unit": "Hours",
    "type": "float",
    "color": "ichou"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

pixel_headers = {
    "X-USER-TOKEN": TOKEN
}

yesterday = dt(2023,9, 10)
today = dt.now()
print(today.strftime("%Y%m%d"))

pixel_config = {
    "date": yesterday.strftime("%Y%m%d"),
    "quantity": "0.5"
}

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=pixel_headers)
# print(response.text)

# Delete pixel
# del_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20230910"
# response = requests.delete(url=del_pixel_endpoint, headers=pixel_headers)
#
# print(response.text)


# Update pixel
pixel_config_upd = {
    "quantity": "3.5"
}

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20230911"
response = requests.put(url=update_pixel_endpoint, headers=pixel_headers, json=pixel_config_upd)

print(response.text)
