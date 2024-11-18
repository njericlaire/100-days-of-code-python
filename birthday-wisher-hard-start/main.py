##################### Hard Starting Project ######################


import pandas
import datetime as dt
import random
import smtplib
birth_day=pandas.read_csv("birthdays.csv")
bd_dict=birth_day.to_dict(orient="records")
print(bd_dict)
now=dt.datetime.now()
month=now.month
day=now.day
my_email="mwangiclaire27@gmail.com"
password="vhle ouda esah dxai"
for i in bd_dict:
    if i["month"]==month and i["day"]==day:
        print("Happy birthday")
    with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as letter:
        send_letter=letter.read()
        send_letter=send_letter.replace("[NAME]",i["name"])
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email,password)
        connection.sendmail(from_addr=my_email,to_addrs=my_email, msg=f"Subject: Happy Birthday\n\n{send_letter}")



# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



