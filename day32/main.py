import smtplib
import datetime as dt
import random

my_email = ""
password = ""

quotes = []

with open("quotes.txt", "r") as f:
    #all_quotes = f.readline()
    for quote in f:
        quotes.append(quote)

aux = random.randint(1, len(quotes))

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()  # Encripta la conexion para hacerla seguro
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="rr.david.marlor@gmail.com",
                        msg=f"Subject:Motivational Quote\n\n{quotes[aux]}")
"""
now = dt.datetime.now()
year = now.year
day_of_week = now.weekday()
print(day_of_week)
print(now)
print(year)

date_of_birthday = dt.datetime(year=1993, month=6, day=24)
print(date_of_birthday)
"""