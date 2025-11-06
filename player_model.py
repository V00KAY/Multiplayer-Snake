from turtle import Turtle
import time

class Player:

    def __init__(self, cor, color, name):

        # Name
        self.name = name
        
        # Head
        self.head = Turtle("square")
        self.head.penup()
        self.head.color(color)
        self.head.direction = "stop"

        self.head.startcor = cor[0], cor[1]
        self.head.goto(self.head.startcor)

        # Body list
        self.body = []

        # Score
        self.score = 0

        # Lives
        self.lives= 3
    
    # Body movement following the head
    def body_move(self):
        if len(self.body) > 0:
            for index in range(len(self.body), 1, -1):
                one_body_part = self.body[index - 1]
                next_body_part = self.body[index - 2]
                one_body_part.goto(next_body_part.xcor(), next_body_part.ycor())
                
            
            self.body[0].goto(self.head.xcor(), self.head.ycor())

    # Body deletion
    def body_delete(self):
        for one_body_part in self.body:
            one_body_part.goto(1500, 1500)
        self.body = []
        self.score = 0

    # Body part deletion
    def body_part_delete(self, index):
        for i in range(len(self.body)-1, index-1, -1):
            one_body_part = self.body[i]
            one_body_part.goto(1500, 1500)
            self.body.remove(one_body_part)
            self.score -= 1

    # Direction setting
    def move_up(self):
        "Set movement direction to up"
        if self.head.direction != "down":
            self.head.direction = "up"

    def move_down(self):
        "Set movement direction to down"
        if self.head.direction != "up":
            self.head.direction = "down"

    def move_left(self):
        "Set movement direction to left"
        if self.head.direction != "right":
            self.head.direction = "left"

    def move_right(self):
        "Set movement direction to right"
        if self.head.direction != "left":
            self.head.direction = "right"


    # Direction execution
    def move(self):
        """Zajištuje pohyb"""
        if self.head.direction == "up":
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

    
    def reset(self):
        time.sleep(0.4)
        self.lives -= 1

        self.body_delete()

        self.head.goto(self.head.startcor)

    def pick_apple(self):

        self.body_part = Turtle("square")
        self.body_part.color("grey")
        self.body_part.penup()

        self.score += 1

        self.body.append(self.body_part)

    def hit_yourself(self):
        for one_body_part in self.body:
            if self.head.distance(one_body_part) < 20:
                self.reset()

    def collision_with_borders(self, min_y, max_y, min_x, max_x):
        if self.head.xcor() > max_x or self.head.xcor() < min_x or self.head.ycor() > max_y or self.head.ycor() < min_y:
            self.reset()

    def collision_with_player(self, opponent):

        self.opponent = opponent

        for index in range(0, len(opponent.body)):
            one_body_part = opponent.body[index]
            if self.head.distance(one_body_part) < 20:
                self.reset()
                opponent.body_part_delete(index)
                break

    def collision_with_apple(self, apple):

        if self.head.distance(apple.body) < 20:
            self.pick_apple()
            apple.apple_teleport() 