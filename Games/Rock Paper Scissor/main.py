# ----- ROCK PAPER SCISSOR -----

import random as r
game_on = True
user_points = 0
com_points = 0
while game_on == True:
    if user_points == 3:
        print("Congrats! You have won the match!")
        break
    elif com_points == 3:
        print("Sorry! Computer have won the match! Try next time!")
        break
    com_pick = r.choice(["r", "p", "s"])
    user_pick = (input("Pick r/p/s for Rock or Paper or Scissor: "))
    print(f"Computer have picked {com_pick}")
    if user_pick == "r" or user_pick == "p" or user_pick == "s":
        if com_pick == user_pick:
            print(f"Its a draw! both picked {user_pick}")
        elif com_pick == "p" and user_pick == "s":
            user_points += 1
            print("You won and got 1 point!")
        elif com_pick == "r" and user_pick == "s":
            com_points += 1
            print("Computer won and got 1 point!")
        elif com_pick == "p" and user_pick == "r":
            com_points += 1
            print("Computer won and got 1 point!")
        elif com_pick == "r" and user_pick == "p":
            user_points += 1
            print("You won and got 1 point!")
        elif com_pick == "s" and user_pick == "r":
            user_points += 1
            print("You won and got 1 point!")
        elif com_pick == "s" and user_pick == "p":
            com_points += 1
            print("Computer won and got 1 point!")
        print(f"Total score: Computer - {com_points} and You - {user_points}.")
    else:
        print("Please choose a valid item.")
