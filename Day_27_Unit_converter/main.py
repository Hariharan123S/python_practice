from tkinter import *

window = Tk()
window.minsize(width=300, height=100)
window.title('Mile to Km Converter')
window.config(padx=10, pady=10)

mile_input = Entry(width=10)
mile_input.grid(row=0, column=1)
km_input = Label(text=0, font=('Times New Roman', 15 , 'bold'))
km_input.grid(row=1, column=1)


def labels():
    label_1 = Label(text='is equal to', font=('Times New Roman', 15 , 'bold'))
    label_1.grid(row=1, column=0)
    label_2 = Label(text='Miles',font=('Times New Roman', 15 , 'bold'))
    label_2.grid(row=0, column=2)
    label_3 = Label(text='Km', font=('Times New Roman', 15 , 'bold'))
    label_3.grid(row=1, column=2)


def text_box():
    value = float(mile_input.get())
    convert = round(value * 1.60934)
    km_input['text'] = convert


button = Button(text='Calculate', font=('Times New Roman', 12, 'bold'), command=text_box)
button.grid(row=2, column=1)
labels()















window.mainloop()
