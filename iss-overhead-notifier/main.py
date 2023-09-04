import requests
from datetime import datetime
import smtplib
import schedule
import time


# Constants
# Manchester, UK
MY_LAT = 53.480759
MY_LONG = -2.242631

SENDER_EMAIL = "aranygyapi@gmail.com"
SENDER_EMAIL_PASS = ""
TARGET_EMAIL = "aranygyapi@gmail.com"


# Function to tell if the ISS is overhead
def iss_overhead():
    """
    Check if the ISS is overhead +- 5 degrees of your location
    Returns 'True' if yes
    """
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Position is within +5 or -5 degrees of the ISS position.
    if (MY_LAT - 5) < iss_latitude < (MY_LAT + 5) and (MY_LONG - 5) < iss_longitude < (MY_LONG + 5):
        return True


def is_dark():
    """
    Check if it's dark outside right now, returns 'True' if yes
    """
    time_now = datetime.now()
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

    if sunset < time_now.hour < sunrise:
        return True


def send_email():
    """
    Send email to specific address
    """
    email_msg = f"Subject:ISS is overhead!\n\nThe ISS is passing overhead, look up!"
    # print(email_msg)  # Debug info

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=SENDER_EMAIL_PASS)
        connection.sendmail(from_addr=SENDER_EMAIL,
                            to_addrs=TARGET_EMAIL,
                            msg=email_msg
                            )


def main_loop():
    if iss_overhead() and is_dark():
        send_email()


# Run every 60 seconds
schedule.every(60).seconds.do(main_loop())

while True:
    schedule.run_pending()
    time.sleep(1)
