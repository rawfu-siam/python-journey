# ----- GUESS THE NUMBER -----
# Rules - the computer will choose a random number between 1 to 100.
#         You have the guess the number in the least possible attempts!
#         the one with the least number of attempts will win!

import random as r

number = r.randint(1,100)
guess = False
total_guess = 1
while guess == False:
    try:
        user_pick = int(input("Select a number from 1 to 100: "))

        if user_pick == 0:
            print("Zeros are not accepted! Select a number from 1 to 100: ")
        elif user_pick < 0:
            print("Negative numbers are not accepted! Select a number from 1 to 100: ")
        elif user_pick > 100:
            print("Sorry! Values higher than 100 is not accepted!")
        
        elif user_pick > 0:
            if user_pick > number :
                print("Choose a number smaller than the current one.")
            elif user_pick < number:
                print("Choose a number bigger than the current one.")
            elif user_pick == number:
                guess = True
                print(f"You have successfully guess the number by {total_guess} attempts which is {number}!")
            total_guess += 1
    except ValueError:
        print("Please enter a valid number!")
print("Congrats! You have completed the game!")
