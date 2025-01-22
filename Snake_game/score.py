from turtle import Turtle, Screen


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())

    def text(self):
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.pendown()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score} ", False, 'center', ('Arial', 15, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def points(self):
        self.score += 1
        self.update_score()







