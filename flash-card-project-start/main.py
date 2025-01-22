from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
current_word = {}
data_dict = {}
try:
    data = pandas.read_csv('data/french_words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    data_dict = original_data.to_dict(orient='records')
else:
    data_dict = data.to_dict(orient='records')


def next_card():
    global current_word
    current_word = random.choice(data_dict)
    canvas.itemconfig(text_title, text='French', fill='black')
    canvas.itemconfig(text_word, text=current_word['French'], fill='black')
    canvas.itemconfig(card, image=photo)
    window.after(3000, func=next_language)

def next_language():
    canvas.itemconfig(text_title, text='English', fill='white')
    canvas.itemconfig(text_word, text=current_word['English'], fill='green')
    canvas.itemconfig(card, image=photo2)

def is_known():
    data_dict.remove(current_word)
    data = pandas.DataFrame(data_dict)
    data.to_csv('data/french_words_to_learn.csv', index=False)

    next_card()

window.after(3000, func=next_language)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
photo = PhotoImage(file='images/card_front.png')
photo2 = PhotoImage(file='images/card_back.png')
card = canvas.create_image(400, 263, image=photo)
canvas.grid(row=0, column=0, columnspan=2)
text_title = canvas.create_text(400, 150, text='title', font=('Arial', 40, 'italic'))
text_word = canvas.create_text(400, 263, text='word', font=('Arial', 60, 'bold'))

photo_right = PhotoImage(file='images/right.png')
button_right = Button(image=photo_right, highlightthickness=0, command=is_known)
button_right.grid(row=1, column=1)

photo_wrong = PhotoImage(file='images/wrong.png')
button_wrong = Button(image=photo_wrong, highlightthickness=0, command=next_card)
button_wrong.grid(row=1, column=0)

next_card()


window.mainloop()

