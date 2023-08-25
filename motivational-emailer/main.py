import smtplib
import datetime as dt
import random


my_email = "aranygyapi@gmail.com"
password = ""

now = dt.datetime.now()
weekday = now.weekday()
# print(weekday)

with open("quotes.txt") as quotes_file:
    quotes = quotes_file.readlines()
    random_quote = random.choice(quotes)
    # print(random_quote)

email_msg = f"Subject:Motivational quote\n\n{random_quote}"

if weekday == 4:

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password )
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=email_msg
                            )
