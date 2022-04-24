from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.Eaten()

    def Eaten(self):
        random_x_num = random.randint(-280, 280)
        random_y_num = random.randint(-280, 280)
        self.goto(random_x_num, random_y_num)
