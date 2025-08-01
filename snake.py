from turtle import Turtle


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create()
        self.head = self.snake_body[0]

    def create(self):
        for i in range(3):
            snake = Turtle(shape="square")
            snake.penup()
            snake.color("white")
            snake.goto(x=0 + i * -20, y=0)
            self.snake_body.append(snake)

    def new_segment(self):
        snake = Turtle(shape="square")
        snake.penup()
        snake.color("white")
        x = self.snake_body[-1].position()
        snake.goto(x)
        self.snake_body.append(snake)

    def move(self):
        for segment in range(len(self.snake_body) - 1, 0, -1):
            new_pos_x = self.snake_body[segment - 1].xcor()
            new_pos_y = self.snake_body[segment - 1].ycor()
            self.snake_body[segment].goto(new_pos_x, new_pos_y)
        self.snake_body[0].forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
