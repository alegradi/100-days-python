import random
import pandas
import datetime as dt
import os
import smtplib


birthdays_today = []
my_email = "aranygyapi@gmail.com"
password = ""

now = dt.datetime.now()

# Load the birthdays csv
birthdays_df = pandas.read_csv("birthdays.csv")

# Convert dataframe to dictionary
birthdays_dict = birthdays_df.to_dict(orient="records")

# List files in directory
email_templates = os.listdir("letter_templates")


# Check month/day in birthdays.csv
def birthday_today():
    for record in birthdays_dict:
        if record["month"] == now.month:
            if record["day"] == now.day:
                birthdays_today.append(record)


def email_birthday_message():
    for record in birthdays_today:
        # Select random email template
        email_template = random.choice(email_templates)
        with open(f"letter_templates/{email_template}", "r") as file:
            file_data = file.read()

        file_data = file_data.replace("[NAME]", record["name"])

        email_msg = f"Subject:Happy Birthday!\n\n{file_data}"
        # print(email_msg)  # Debug info

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=record["email"],
                                msg=email_msg
                                )


birthday_today()
if len(birthdays_today) != 0:

    # print(birthdays_today)  # Debug info
    email_birthday_message()














# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




