from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # Collision with food
    if snake.head.distance(food) <= 15:
        food.refresh()
        scoreboard.add_score()
        snake.extend()

    # Collision with wall
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        snake.reset()
        scoreboard.reset_score()

    # Collision with tail
    for segment in snake.all_segments[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            snake.reset()
            scoreboard.reset_score()

screen.exitonclick()
