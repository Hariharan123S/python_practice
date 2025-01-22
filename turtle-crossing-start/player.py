from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)

    def start_pos(self):
        self.goto(STARTING_POSITION)

    def mov_up(self):
        self.forward(10)

    def finish(self):
        if self.ycor() > 280:
            return True
        else:
            return False

