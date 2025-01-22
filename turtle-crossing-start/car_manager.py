from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def new_car(self):
        rd_chance = random.randint(1, 6)
        if rd_chance == 1:
            car = Turtle()
            car.shape('square')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            new_x = random.randint(290, 300)
            new_y = random.randint(-250, 250)
            car.goto(new_x, new_y)
            car.color(random.choice(COLORS))
            self.all_cars.append(car)

    def car_mov(self):
        for i in self.all_cars:
            i.back(self.speed)

    def nxt_level(self):
        self.speed += MOVE_INCREMENT






