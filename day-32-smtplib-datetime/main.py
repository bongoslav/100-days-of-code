import random
import smtplib
import datetime as dt
import pandas

my_email = ""
password = ""

now = dt.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")

# get the dict in format: (month, day): *all the data for row*
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    birthday_person = birthday_dict[today]  # birthday_dict has keys (birthday month, birthday day)
    filepath = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(filepath) as wish_file:
        contents = wish_file.read()
        contents = contents.replace("[NAME]", birthday_person['name'])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday\n\n{contents}")