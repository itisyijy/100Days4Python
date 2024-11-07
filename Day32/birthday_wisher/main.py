# Day32 for 100Days4Python
# Project for Day32 : Birthday Wisher!

import random
import pandas
import smtplib
import datetime

birthday_csv = pandas.read_csv("./birthdays.csv")
birthday_dict = birthday_csv.to_dict(orient="records")

now = datetime.datetime.now()
month = now.month
day = now.day

from_address = "itisyijy@gmail.com"
to_address = "graycona@yahoo.com"

for person in birthday_dict:
    if person["month"] == month and person["day"] == day:
        with open(f"./letter_templates/letter_{random.randint(1, 3)}.txt") as letter_file:
            letter = letter_file.read()
            letter = letter.replace("[NAME]", f"{person["name"]}")
        
        with smtplib.SMTP("smtp.gmail.com") as gmail:
            gmail.starttls()
            gmail.login(user=from_address, password=input("PASSWORD: "))
            gmail.sendmail(from_addr=from_address, to_addrs=to_address,
                           msg=f"Subject:Happy Birthday!\n\n{letter}")
