from turtle import Turtle
import time
import random

class Apple:

    def __init__(self):
        self.body = Turtle("circle")
        self.body.color("purple")
        self.body.penup()

    def apple_teleport(self):
        random_x = random.randint(-480, 481)
        random_y = random.randint(-480, 481)
        self.body.goto(random_x, random_y)