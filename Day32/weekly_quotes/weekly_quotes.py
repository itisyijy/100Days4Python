# Day32 for 100Days4Python
# Project for Day32 : Weekly Motivation Quotes

import random
import smtplib
import datetime

MONDAY = 0
TUESDAY = 1
WEDNESDAY = 2
THURSDAY = 3
FRIDAY = 4
SATURDAY = 5
SUNDAY = 6

now = datetime.datetime.now()
if now.weekday() == THURSDAY:
    my_address = "itisyijy@gmail.com"
    to_address = "graycona@yahoo.com"
    my_password = input(f"{my_address}\nPASSWORD >>> ")
    
    with open("./quotes.txt") as file:
        quotes_list = file.readlines()

    quote_of_the_day = random.choice(quotes_list)
    with smtplib.SMTP("smtp.gmail.com") as gmail:
        gmail.starttls()
        gmail.login(user=my_address, password=my_password)
        gmail.sendmail(from_addr=my_address, to_addrs=to_address,
                       msg=f"Subject:!WEEKLY MOTIVATION QUOTE!\n\n{quote_of_the_day}")
