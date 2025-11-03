from turtle import Turtle
import time

class Player:

    def __init__(self, cor, color, name):

        # Základní nastavení hráče při startů
        # ------------

        # Jméno
        self.name = name
        
        # Hlava
        self.head = Turtle("square")
        self.head.penup()
        self.head.color(color)
        self.head.direction = "stop"

        self.head.startcor = cor[0], cor[1]
        self.head.goto(self.head.startcor)

        # Tělo
        self.body = []

        # Skore
        self.score = 0

        # Životy
        self.lives= 3
    
    # Pohyb těla za hlavou
    def body_move(self):
        if len(self.body) > 0:
            for index in range(len(self.body), 1, -1):
                one_body_part = self.body[index - 1]
                next_body_part = self.body[index - 2]
                one_body_part.goto(next_body_part.xcor(), next_body_part.ycor())
                
            
            self.body[0].goto(self.head.xcor(), self.head.ycor())

    # Vymazání těla
    def body_delete(self):
        for one_body_part in self.body:
            one_body_part.goto(1500, 1500)
        self.body = []
        self.score = 0

    # Vymazání části těla
    def body_part_delete(self, index):
        for i in range(len(self.body)-1, index-1, -1):
            one_body_part = self.body[i]
            one_body_part.goto(1500, 1500)
            self.body.remove(one_body_part)
            self.score -= 1

    # Nastavení směru
    def move_up(self):
        "Nastaví pohyb nahoru"
        if self.head.direction != "down":
            self.head.direction = "up"

    def move_down(self):
        "Nastaví pohyb dolu"
        if self.head.direction != "up":
            self.head.direction = "down"

    def move_left(self):
        "Nastaví pohyb doleva"
        if self.head.direction != "right":
            self.head.direction = "left"

    def move_right(self):
        "Nastaví pohyb doprava"
        if self.head.direction != "left":
            self.head.direction = "right"


    # Provedení směru
    def move(self):
        """Zajištuje pohyb"""
        if self.head.direction == "up":
            # Vezme aktuální souřadnici Y a k ní přičítá pohyb nahoru
            y = self.head.ycor()
            self.head.sety(y + 20) 
        elif self.head.direction == "down":
            y = self.head.ycor()
            self.head.sety(y - 20) 
        elif self.head.direction == "left":
            x = self.head.xcor()
            self.head.setx(x - 20) 
        elif self.head.direction == "right":
            x = self.head.xcor()
            self.head.setx(x + 20) 

    

