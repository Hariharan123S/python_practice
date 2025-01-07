from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.x_mov = 10
        self.y_mov = 10
        self.mov_speed = 0.1

    def mov_ball(self):
        new_x = self.xcor() + self.x_mov
        new_y = self.ycor() + self.y_mov
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_mov *= -1

    def bounce_opp(self):
        self.x_mov *= -1
        self.mov_speed *= 0.9
