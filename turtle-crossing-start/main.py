import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.mov_up, "Up")
# screen.onkey(player.,'Down' )

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.new_car()
    car_manager.car_mov()

    for i in car_manager.all_cars:
        if i.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.finish():
        scoreboard.nxt_level()
        player.start_pos()
        car_manager.nxt_level()

screen.exitonclick()
