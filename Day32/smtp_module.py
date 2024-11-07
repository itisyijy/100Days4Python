# Day32 for 100Days4Python
# Day32 : Email SMTP

import smtplib

from_email = "itisyijy@gmail.com"
from_password = input(f"{from_email}\nPASSWORD : ")

to_email = "graycona@yahoo.com"

# TLS, Transport Layer Security. Protocol Designed to Secure and Encrypt Communications over a Computer Network

# gmail_connection = smtplib.SMTP("smtp.gmail.com")
# gmail_connection.starttls()
# gmail_connection.login(user=from_email, password=from_password)
# gmail_connection.sendmail(from_addr=from_email, to_addrs=to_email,
#                           msg="Subject:Hello\n\nThis is the body of email.")
# gmail_connection.close()

with smtplib.SMTP("smtp.gmail.com") as gmail_connection:
    gmail_connection.starttls()
    gmail_connection.login(user=from_email, password=from_password)
    gmail_connection.sendmail(from_addr=from_email, to_addrs=to_email,
                              msg="Subject:Hello\n\nThis is the body of email.")    # \n\n ~ body
