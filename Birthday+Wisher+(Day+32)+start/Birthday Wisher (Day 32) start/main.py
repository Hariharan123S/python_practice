import smtplib
import random
import datetime as dt




my_email = 'abcd2025py@gmail.com'
password = "tufyqhaftnwzdngr"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 6:
    with open("quotes.txt") as data:
        quote = data.readlines()
        data_quote = random.choice(quote)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="harithasomu27@gmail.com",
            msg=f"Subject:Sunday Motivation\n\n{data_quote}"
        )












































'''my_mail = "abcd2025py@gmail.com"
password = "tufyqhaftnwzdngr"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_mail, password=password)
    connection.sendmail(
        from_addr=my_mail,
        to_addrs="abcd2025py@gmail.com",
        msg="Subject:Hello!\n\nThis is the body of the mail."
    )'''
#import datetime as dt
#now = dt.datetime.now()
#year = now.year
#print(now)
#month = now.month
#print(month)
#day_of_week = now.weekday()
#print(day_of_week)
#
#dob = dt.datetime(year=2002, month=11, day=6, hour=11)
#print(dob)
