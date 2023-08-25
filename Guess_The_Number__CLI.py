"""
Author: 
    Donald Saulny III
Project: 
    Guess The Number - CLI Version
Description:
    Users are given 5 chances to guess the number between 0 and 100
    Upon each entry, the user is told whether the number is higher or lower
    If the user guess the number at any point, the user wins the game
    If the user does not guess the number by their 5th turn, the user loses
"""

import os
import random

def guessTheNumber():
    
    # clean terminal
    os.system("cls") if os.name == "nt" else os.system("clear")
   
    # game instructions
    print("\n\nWelcome to Guess The Number!!!\n\n" +
        "Instructions:\n\t" +
        "You get 5 attempts to guess the number.\n\t" +
        "The number exists in the range 0-100.\n\t" +
        "After each guess, you'll be told whether the number is higher or lower.\n\t" +
        "Let's get started!!!\n")
    
    # variables
    number = random.randint(1,99)
    victory = False
    
    # game
    for _ in range(5):
        
        # user input
        while True:
            try:
                guess = int(input("Enter your guess: "))
                break
            except:
                print("Invalid input, try again.\n")
    
        if number == guess: 
            print(f"Congratulations!!! You won!!! The number was {guess}.\n")
            victory = True
            break

        else:
            number > guess and print(f"The number is higher than {guess}.\n")
            number < guess and print(f"The number is lower than {guess}.\n")

    victory == False and print(f"You lose. The number was {number}\n")
    
    # play again
    while True:
        p = input("Play again? (Y/N): ")
        try:
            if p == 'y':
                guessTheNumber()

            elif p =='n':
                print("Thank you for playing.\n\n")
                exit()

            elif p not in ('n', 'y'):
                raise ValueError
            
        except ValueError:
            print("Invalid input, try again.\n")

guessTheNumber()
