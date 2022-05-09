# send an SMS to my phone if it's going to rain in the next 12 hours using twilio & openweather API
# and implementing the code in pythoneverywhere.com with reformatting according to docs to run daily
# personal details have been omitted

import requests
from twilio.rest import Client

# we can use environment variables for these (in pythoneverywhere as well)
API_KEY = "API_KEY"
account_sid = "ACCOUNT_SID"
auth_token = "AUTH_TOKEN"

PARAMETERS = {
    "lat": 42.6975,
    "lon": 23.3242,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=PARAMETERS)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["hourly"][:12]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:  # according to openweathermap docs
        will_rain = True

if will_rain:
    # from twilio
    client = Client(account_sid, auth_token)
    message = client.messages.create(
            body="Bring an umbrella ☔.",
            from_='+FROM_NUM',
            to='+MY_NUM'
            )
    print(message.status)