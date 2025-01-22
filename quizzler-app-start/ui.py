from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizzInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.text = self.canvas.create_text(150, 125, text="Amazon acquired Twitch....", width=280, font=('Arial', 20, 'italic'), fill=THEME_COLOR)

        self.photo_tick = PhotoImage(file='images/true.png')
        self.tick_button = Button(image=self.photo_tick, highlightthickness=0, command=self.true_pressed)
        self.tick_button.grid(row=2, column=0)

        self.photo_wrong = PhotoImage(file='images/false.png')
        self.wrong_button = Button(image=self.photo_wrong, highlightthickness=0, command=self.false_pressed)
        self.wrong_button.grid(row=2, column=1)

        self.lable = Label(text="Score: 0", fg='white', bg=THEME_COLOR)
        self.lable.grid(row=0, column=1)

        self.next_question()


        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.canvas.config(bg='white')
            self.lable.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="You,ve reached the end of the quiz")
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.next_question)


