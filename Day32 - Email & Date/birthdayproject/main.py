import os
from dotenv import load_dotenv
import smtplib
import datetime as dt
import random
import csv

load_dotenv()

my_email = os.getenv("EMAIL_ADDRESS")
password = os.getenv("EMAIL_PASSWORD")

now = dt.datetime.now()
today_month = now.month
today_day = now.day

birthday_people = []

with open('birthdays.csv') as file:
    data = csv.DictReader(file)
    
    for row in data:
        if int(row["month"]) == today_month and int(row["day"]) == today_day:
            birthday_people.append(row)

if birthday_people:
    for person in birthday_people:

        letter_number = random.randint(1, 3)
        with open(f'letter_templates/letter_{letter_number}.txt') as letter_file:
            content = letter_file.read()

        personalized_letter = content.replace("[NAME]", person["name"])

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=person["email"],
                msg=f"Subject:Happy Birthday!\n\n{personalized_letter}"
            )

print("yes")

