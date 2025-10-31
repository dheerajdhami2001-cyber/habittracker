import requests
from datetime import datetime

USERNAME = "makeityourselfifavaliable"
TOKEN = "youhavetomakeityourself"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

"""
👉 Uncomment the following two lines ONLY ONCE when setting up your Pixela account.
   These create your graph. Run once, then keep commented.
"""
# responses = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(responses.text)

"""
👉 Uncomment the following two lines ONLY if your Pixela user account is not yet created.
   It registers your user. Run once, then keep commented.
"""
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"

today = datetime.now()
formate_today = today.strftime("%Y%m%d")

pixel_config = {
    "date": formate_today,
    "quantity": input("how much did you cycle today????")
}

# This line adds a new pixel (entry) for today's date.
response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/20251028"

update_params = {
    "quantity": input("what to change ?????")
}

"""
👉 Uncomment the following two lines ONLY when you want to update an existing pixel entry.
   Make sure the date (here 20251028) exists before updating.
"""
# response = requests.put(url=pixel_update_endpoint, json=update_params, headers=headers)
# print(response.text)

pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/20251028"

"""
⚠️ Uncomment the following two lines ONLY when you want to delete a specific pixel entry.
   Be careful: this will permanently remove that pixel’s data.
"""
# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)