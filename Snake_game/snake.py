from turtle import Turtle


POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.new_seg = []
        self.create_snake()
        self.head = self.new_seg[0]

    def create_snake(self):
        for i in POSITION:
            self.add_seg(i)

    def add_seg(self, i):
        square = Turtle("square")
        square.color("white")
        square.penup()
        square.goto(i)
        self.new_seg.append(square)

    def reset(self):
        for seg in self.new_seg:
            seg.goto(1000, 1000)
        self.new_seg.clear()
        self.create_snake()
        self.head = self.new_seg[0]

    def extend(self):
        self.add_seg(self.new_seg[-1].position())


    def snake_mov(self):
        for seq_num in range(len(self.new_seg) - 1, 0, -1):
            new_x = self.new_seg[seq_num - 1].xcor()
            new_y = self.new_seg[seq_num - 1].ycor()
            self.new_seg[seq_num].goto(new_x, new_y)
        self.head.forward(MOVE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
