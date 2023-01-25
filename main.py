import requests

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


response = requests.post(graph_endpoint, json=graph_config, headers=headers)
print(response.text)
