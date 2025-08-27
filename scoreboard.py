from turtle import Turtle

ALIGNMENT = "center"
FONT = "Courier"
FONT_SIZE = 16
TYPE = "normal"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(x=0, y=270)
        self.color("white")
        self.points = 0
        self.write(f"Score: {self.points} ", False, align=ALIGNMENT, font=(FONT, FONT_SIZE, TYPE))

    def game_over(self):
        self.penup()
        self.goto(30, 0)
        self.write(f"GAME OVER!  ", False, align=ALIGNMENT, font=(FONT, FONT_SIZE, TYPE))

    def point_up(self):
        self.points += 1
        self.clear()
        self.write(f"Score: {self.points} ", False, align=ALIGNMENT, font=(FONT, FONT_SIZE, TYPE))

