import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_on = True
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_on:
    screen.update()
    time.sleep(0.09)
    snake.move()
    if snake.head.distance(food) < 15:
        food.spawn()
        scoreboard.point_up()
        snake.new_segment()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()
    for segments in snake.snake_body[1:]:
        if snake.head.distance(segments) < 10:
            game_on = False
            scoreboard.game_over()


screen.exitonclick()
