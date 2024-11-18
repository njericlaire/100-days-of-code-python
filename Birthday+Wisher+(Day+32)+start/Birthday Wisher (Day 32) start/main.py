import smtplib


import datetime as dt
import random

now=dt.datetime.now()

day_of_the_week=now.weekday()

my_email="mwangiclaire27@gmail.com"
password="vhle ouda esah dxai"

if day_of_the_week==0:
    with open("quotes.txt") as quote_file:
        all_quotes=quote_file.readlines()
        quote= random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(from_addr=my_email,to_addrs=my_email, msg=f"Subject: Monday Motivation\n\n{quote}")

#

