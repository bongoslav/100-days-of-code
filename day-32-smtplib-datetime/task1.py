import datetime as dt
import smtplib
import random

my_email = "gpetar96@gmail.com"
password = "!Bubole4kata1"

now = dt.datetime.now()
current_weekday = now.weekday()
if current_weekday == now.weekday():
    with open("quotes.txt") as quotes_file:
        quotes_list = quotes_file.readlines()
        quote = random.choice(quotes_list)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="darkridercap@yahoo.com",
                            msg=f"Subject: motivation\n\n{quote}")

connection.close()