from player_model import Player
from turtle import Turtle, Screen
import time
import random

# Základní nastavení screenu
game_screen = Screen()
game_screen.bgcolor("green")
game_screen.setup(1000, 1000)
game_screen.tracer(False)

# Stats hráč 1
# --------
stats1 = Turtle()
stats1.hideturtle()
stats1.penup()
stats1.goto(-430, 430)
stats1.write("Hráč 1\nSkore: 0\nŽivoty: 3", align="center", font=("Courier", 13, "bold"))
 
# Stats hráč 2
# --------
stats2 = Turtle()
stats2.hideturtle()
stats2.penup()
stats2.goto(430, 430)
stats2.write("Hráč 2\nSkore: 0\nŽivoty: 3", align="center", font=("Courier", 13, "bold"))

# Hráč 1
# --------
player1 = Player([-250, 0], "black", "Hráč 1")


# Hráč 2
# --------
player2 = Player([250, 0], "white", "Hráč 2")


# Jablíčko
# --------
apple = Turtle("circle")
apple.color("purple")
apple.penup()


# Vyvolání funkce klávesami hráč 1
game_screen.listen() # Začně poslouchat události
game_screen.onkeypress(player1.move_up, "w")
game_screen.onkeypress(player1.move_down, "s")
game_screen.onkeypress(player1.move_left, "a")
game_screen.onkeypress(player1.move_right, "d")

# Vyvolání funkce klávesami hráč 2
game_screen.onkeypress(player2.move_up, "Up")
game_screen.onkeypress(player2.move_down, "Down")
game_screen.onkeypress(player2.move_left, "Left")
game_screen.onkeypress(player2.move_right, "Right")

# Funkce

def new_body_part(): 
    body_part = Turtle("square")
    body_part.color("grey")
    body_part.penup()
    return body_part

def stats_update():
    stats1.clear()
    stats1.write(f"Hráč 1\nSkore: {player1.score}\nŽivoty: {player1.lives}", align="center", font=("Courier", 13, "bold"))

    stats2.clear() 
    stats2.write(f"Hráč 2\nSkore: {player2.score}\nŽivoty: {player2.lives}", align="center", font=("Courier", 13, "bold"))

def reset(who):
    time.sleep(0.4)
    who.lives -= 1

    who.body_delete()
    stats_update()

    who.head.goto(who.head.startcor)

def apple_teleport():
    random_x = random.randint(-480, 481)
    random_y = random.randint(-480, 481)
    apple.goto(random_x, random_y)
apple_teleport()

def pick_apple(who):
    apple_teleport()

    who.score += 1

    stats_update()

    who.body.append(new_body_part())

def hit_yourself(who):
    for one_body_part in who.body:
        if who.head.distance(one_body_part) < 20:
            reset(who)

def winorlost():
    global playgame, winner, how

    for player, opponent in [(player1, player2), (player2, player1)]:
        if player.lives == 0:
            winner = opponent.name
            time.sleep(0.3)
            game_screen.bye()
            playgame = False
            how = "smrt"
        elif player.score >= 10:
            winner = player.name
            time.sleep(0.3)
            game_screen.bye()
            playgame = False
            how = "skore"


# Cyklus hry
playgame = True
while playgame == True:

    # Kontrola života
    winorlost()
    if playgame == False:
        break

    # Konstrola kolize s okraji
    if player1.head.xcor() > 490 or player1.head.xcor() < -490 or player1.head.ycor() > 490 or player1.head.ycor() < -490:
        reset(player1)
    
    if player2.head.xcor() > 490 or player2.head.xcor() < -490 or player2.head.ycor() > 490 or player2.head.ycor() < -490:
        reset(player2)

    # Kontrola s vlastním tělem
    hit_yourself(player1)
    hit_yourself(player2)

    # Kolize Hráče 1 z jiným tělem
    for index in range(0, len(player2.body)):
        one_body_part = player2.body[index]
        if player1.head.distance(one_body_part) < 20:
            reset(player1)
            player2.body_part_delete(index)
            stats_update()
            break

    # Kolize Hráče 2 z jiným tělem
    for index in range(0, len(player1.body)):
        one_body_part = player1.body[index]
        if player2.head.distance(one_body_part) < 20:
            reset(player2)
            player1.body_part_delete(index)
            stats_update()
            break

    # Co se stane po dotknutí jablíčka
    if player1.head.distance(apple) < 20:
        pick_apple(player1)
    elif player2.head.distance(apple) < 20:
        pick_apple(player2)

    # Pohyb těla 
    player1.body_move()
    player2.body_move()

    # Pohnutí
    player1.move()
    player2.move()
    time.sleep(0.07)

    # Znova updaitnutí obrazovky
    game_screen.update()

win_screen = Screen()
win_screen.bgcolor("green")
win_screen.setup(500, 500)
win_screen.tracer(False)


# TEXT
# --------
win_text = Turtle()
win_text.hideturtle()
win_text.penup()
win_text.goto(0, 0)

if how == "smrt":
    win_text.write(f"Vyhral {winner}\nProtihráč spráchal sebeznežití.", align="center", font=("Courier", 13, "bold"))
else:
    win_text.write(f"Vyhral {winner}\nPrvní nasbíral skore.", align="center", font=("Courier", 13, "bold"))




win_screen.exitonclick()