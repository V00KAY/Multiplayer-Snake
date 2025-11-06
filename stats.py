from turtle import Turtle
import time
import random

class Stats:

    def __init__(self, cor, name):
        self.cor = cor[0], cor[1]
        self.name = name

        self.text = Turtle()
        self.text.hideturtle()
        self.text.penup()
        self.text.goto(self.cor)
        self.text.write(f"{self.name}\nScore: 0\nLives: 3", align="center", font=("Courier", 13, "bold"))
    
    def stats_update(self, score, lives):
        self.text.clear()
        self.text.write(f"{self.name}\nScore: {score}\nLives: {lives}", align="center", font=("Courier", 13, "bold"))