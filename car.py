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
        self.goto(300, random.randint(-250, 250))
        self.showturtle()

    def move(self, speed):
        self.backward(speed)
