import requests
import datetime as dt

USERNAME = 'alonzo123'
TOKEN = 'hkl123456'

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
  "token": TOKEN,
  "username": USERNAME,
  "agreeTermsOfService": "yes",
  "notMinor": 'yes'
}

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
  "id": 'graph1',
  "name": 'Coding Graph',
  "unit": 'Day',
  "type": 'int',
  "color": 'ajisai'
}

headers = {
  "X-USER-TOKEN": TOKEN
}


# response = requests.post(graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
#

pixel_endpoint = f"{graph_endpoint}/graph1"

now = dt.datetime.now()
print(now)
date = f"{now.year}{now.month}{now.day}"
print(date)
pixel_config = {
  'date': date,
  'quantity': '1'
}

response = requests.post(pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)
