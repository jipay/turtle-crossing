from turtle import Turtle
import random


class Car(Turtle):
    def __init__(self, color):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(color)
        self.goto(random.choice(range(300, 460, 40)), random.choice(range(-240, 240, 30)))
        self.showturtle()

    def move(self, speed):
        self.goto(self.xcor() - speed, self.ycor())
