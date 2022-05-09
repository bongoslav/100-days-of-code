import requests
from datetime import datetime as dt

# ISS location API practice
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (latitude, longitude)
# print(iss_position)

# Sunrise/sunset API
MY_LAT = 42.697708
MY_LONG = 23.321867

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]  # note: it's utc time
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]  # get the hours only

print(sunrise)
print(sunset)

time_now = dt.now()
print(time_now.hour)