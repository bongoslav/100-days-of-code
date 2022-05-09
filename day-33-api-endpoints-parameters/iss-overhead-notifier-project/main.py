import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 42.697708  # Your latitude
MY_LONG = 23.321867  # Your longitude
MY_EMAIL = "anemail@mail.com"
EMAIL_PASSWORD = "apassword"
port = 465

def iss_is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if sunset <= time_now.hour or sunrise >= time_now.hour:
        return True


while True:
    time.sleep(60)  # wait 60s between running the loop
    if iss_is_overhead() and is_night():
        with smtplib.SMTP_SSL("smtp.gmail.com", port) as server:
            server.starttls()
            server.login(MY_EMAIL, EMAIL_PASSWORD)
            server.sendmail(MY_EMAIL, "receiver@mail.com", "Subject: ISS POSITION\n\nISS IS OVERHEAD NOW!")