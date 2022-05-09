import requests
from bs4 import BeautifulSoup
import smtplib
import os

# constants
MY_EMAIL = os.environ["GMAIL"]
MY_PASSWORD = os.environ["GMAIL_PASSWORD"]
BUY_PRICE = 90

url = "https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ/ref=sr_1_1_sspa?crid=3H57JTPXOGYGB&keywords=Instant+Pot&qid=1650726929&s=home-garden&sprefix=instant+pot+%2Cgarden%2C188&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzTllVNDUyRzZBRTMxJmVuY3J5cHRlZElkPUEwMzkwMTMyMkROTkFIVjdJR0lGVyZlbmNyeXB0ZWRBZElkPUEwNjU5MzgxMUk3TVlIVjlIVExFTCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
header = {
    "Accept-Language": "en-US,en;q=0.9,bg-BG;q=0.8,bg;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
}
respond = requests.get(url, headers=header)

soup = BeautifulSoup(respond.text, "lxml")

item_price = float(soup.find(name="span", class_="a-offscreen").text.strip("$"))

# send an email if the price drops below BUY_PRICE
if item_price <= BUY_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="beborisov99@gmail.com",
            msg=f"Subject: Item price alert!\n\nThe selected item is now priced at: {item_price}!"
        )

# Note: if the script is useful if executed daily