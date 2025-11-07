from player_model import Player
from apple import Apple
from stats import Stats
from turtle import Turtle, Screen
import time
import random

def main():
    # Basic screen setup
    game_screen = Screen()
    game_screen.bgcolor("green")
    game_screen.setup(1000, 1000)
    game_screen.tracer(False)

    # Objects
    # --------
    player1 = Player([-250, 0], "black", "Player 1")
    player2 = Player([250, 0], "white", "Player 2")

    stats1 = Stats([-430, 430], player1.name)
    stats2 = Stats([430, 430], player2.name)

    apple = Apple()

    # Triggering functions with keys
    game_screen.listen() 
    game_screen.onkeypress(player1.move_up, "w")
    game_screen.onkeypress(player1.move_down, "s")
    game_screen.onkeypress(player1.move_left, "a")
    game_screen.onkeypress(player1.move_right, "d")

    game_screen.onkeypress(player2.move_up, "Up")
    game_screen.onkeypress(player2.move_down, "Down")
    game_screen.onkeypress(player2.move_left, "Left")
    game_screen.onkeypress(player2.move_right, "Right")

    # Functions

    def winorlost():
        for player, opponent in [(player1, player2), (player2, player1)]:
            if player.lives == 0:
                time.sleep(0.3)
                game_screen.bye()
                playgame = False
                winner = opponent.name
                how = "dead"
                return [playgame, winner, how]
            elif player.score >= 10:
                time.sleep(0.3)
                game_screen.bye()
                playgame = False
                winner = player.name
                how = None
                return [playgame, winner, how]
        return [True, None, None]

    # Game loop
    playgame = True
    apple.apple_teleport()
    while playgame == True:

        # Life check
        variable_list = winorlost()
        playgame, winner, how = variable_list[0], variable_list[1], variable_list[2]
        if playgame == False:
            break

        # Check collision with the game borders
        player1.collision_with_borders(-490, 490, -490, 490)
        player2.collision_with_borders(-490, 490, -490, 490)

        # Check collision with own body
        player1.hit_yourself()
        player2.hit_yourself()

        # Check collision of Players with another body
        player1.collision_with_player(player2)
        player2.collision_with_player(player1)

        # Apple is touched
        player1.collision_with_apple(apple)
        player2.collision_with_apple(apple)

        # Body movement
        player1.body_move()
        player2.body_move()

        # Move
        player1.move()
        player2.move()
        time.sleep(0.07)

        # Stats update
        stats1.stats_update(player1.score, player1.lives)
        stats2.stats_update(player2.score, player2.lives)

        # Update the screen again
        game_screen.update()

    win_screen = Screen()
    win_screen.bgcolor("green")
    win_screen.setup(500, 500)
    win_screen.tracer(False)

    # Win text
    # --------
    win_text = Turtle()
    win_text.hideturtle()
    win_text.penup()
    win_text.goto(0, 0)

    if how == "dead":
        win_text.write(f"Winner {winner}\nThe opponent committed self-destruction.", align="center", font=("Courier", 13, "bold"))
    else:
        win_text.write(f"Winner {winner}\nCollected the score first.", align="center", font=("Courier", 13, "bold"))

    win_screen.exitonclick()

if __name__ == "__main__":
    main()