import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.color("red")
        self.spawn()

    def spawn(self):
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 260)
        self.goto(x=rand_x, y=rand_y)
