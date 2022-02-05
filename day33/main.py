import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.status_code)
# if response.status_code != 200:
# print("Error")
# raise Exception("Bad response from ISS API")
response.raise_for_status()

data = response.json()["iss_position"]
print(data)

data_iss = response.json()
print(data_iss)

longitude = data_iss["iss_position"]["longitude"]
latitude = data_iss["iss_position"]["latitude"]

iss_position = (longitude, latitude)

# Lat Long Cordoba (37.888176, -4.779383)

print(iss_position)
