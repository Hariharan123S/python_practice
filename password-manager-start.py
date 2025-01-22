from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gene_paswd():
    password_text.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password_final = "".join(password_list)
    # password = ""
    # for char in password_list:
    #  password += char

    password_text.insert(0, password_final)
    pyperclip.copy(password_final)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def data_save():
    website_data = website_text.get()
    email_user_data = email_text.get()
    password_data = password_text.get()
    new_data = {
        website_data: {
            "email": email_user_data,
            "password": password_data,
        }
    }

    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="Oops", message="Please fill all the details!")

    else:
        try:
            with open('data.json', mode='r') as data:
                # Reading old data
                datas = json.load(data)
        # Updating old data with new data
        except FileNotFoundError:
            with open('data.txt.json', 'w') as data:
                json.dump(new_data, data, indent=4)
        else:
            datas.update(new_data)

            # Saving updated data
            with open('data.json', mode='w') as data:
                json.dump(datas, data, indent=4)
        finally:
            # data.write(f"{website_data} / {email_user_data} / {password_data}\n")
            website_text.delete(0, END)
            password_text.delete(0, END)


def find_password():
    website_ = website_text.get()
    try:
        with open('data.json', 'r') as data:
            da = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='Data not found')
    else:
        if website_ in da:
            email = da[website_]['email']
            paswd = da[website_]['password']
            messagebox.showinfo(title=website_, message=f"email: {email}\npassword: {paswd}")
        else:
            messagebox.showinfo(title='Error', message=f'No details found on {website_} exists.')


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

website = Label(text='Website:')
website.grid(row=1, column=0)

email_user = Label(text='Email/Username:')
email_user.grid(row=2, column=0)

password = Label(text='Password:')
password.grid(row=3, column=0)

website_text = Entry(width=32)
website_text.focus()
website_text.grid(row=1, column=1)

email_text = Entry(width=51)
email_text.insert(0, 'abcd@gamil.com')
email_text.grid(row=2, column=1, columnspan=2)

password_text = Entry(width=32)
password_text.grid(row=3, column=1)

gene_password = Button(text='Generate Password', command=gene_paswd)
gene_password.grid(row=3, column=2)

add = Button(text='Add', width=44, command=data_save)
add.grid(row=4, column=1, columnspan=2)

search = Button(text='Search', width=14, command=find_password)
search.grid(row=1, column=2)

window.mainloop()
