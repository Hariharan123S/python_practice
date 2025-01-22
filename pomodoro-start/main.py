from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_re = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer_re)
    canvas.itemconfig(text, text="00:00")
    timer.config(text="Timer")
    check_tick.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_time():
    global reps
    reps += 1
    work_time = WORK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    if reps % 2 == 0:
        timer.config(text='Break', fg=PINK)
        count_down(short_break)
    if reps % 8 == 0:
        timer.config(text='Break', fg=RED)
        count_down(long_break)
    else:
        timer.config(text='Work', fg=GREEN)
        count_down(work_time)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_re
        timer_re = window.after(1000, count_down, count - 1)
    else:
        start_time()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"
        check_tick.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=photo)
text = canvas.create_text(100, 130, text='00:00', fill='white', font=('Arial', 35, 'bold'))
canvas.grid(row=1, column=1)

timer = Label(text='Timer', font=(FONT_NAME, 35, 'bold'), bg=YELLOW, fg=GREEN)
timer.grid(row=0, column=1)

start = Button(text='Start', width=5, font=(FONT_NAME, 10, 'bold'), command=start_time)
start.grid(row=2, column=0)

reset = Button(text='Reset', width=5, font=(FONT_NAME, 10, 'bold'), command=reset_timer)
reset.grid(row=2, column=2)

check_tick = Label(text='', fg=GREEN, bg=YELLOW, font='bold')
check_tick.grid(row=3, column=1)

window.mainloop()
