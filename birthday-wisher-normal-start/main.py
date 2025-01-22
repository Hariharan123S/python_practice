##################### Normal Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib
my_email = 'abcd2025py@gmail.com'
password = "tufyqhaftnwzdngr"
today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
new_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in new_dict:
    birthday_Person = new_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]", birthday_Person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_Person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )

