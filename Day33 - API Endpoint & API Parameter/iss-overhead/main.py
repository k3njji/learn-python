import requests
from datetime import datetime
import smtplib
import os

MY_LAT = -6.2369 # Your latitude
MY_LONG = 106.853 # Your longitude

my_email = os.getenv("EMAIL_ADDRESS")
password = os.getenv("EMAIL_PASSWORD")

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.utcnow()
time = time_now.hour
print(sunset)
print(time)

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

if((MY_LAT-5 <= iss_latitude and MY_LAT+5 >= iss_latitude) and (MY_LONG-5 <= iss_longitude and MY_LONG+5 >= iss_longitude)):
    if(time >= sunset or time <= sunrise):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs='harsantokenzie@gmail.com',
                msg=f"Subject:LOOK UP!!!\n\nLOOK UP AT THE SKY STEWPID"
            )