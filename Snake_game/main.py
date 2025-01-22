import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Byte")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
score.text()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_mov()
    if snake.head.distance(food) < 20:
        score.clear()
        snake.extend()
        score.points()
        food.refresh()

    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    for segments in snake.new_seg[1:]:
        if snake.head.distance(segments) < 10:
            score.reset()
            snake.reset()






screen.exitonclick()
