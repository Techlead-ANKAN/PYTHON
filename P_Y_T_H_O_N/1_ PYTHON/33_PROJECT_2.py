# Prohect 2 - The Perfect Guess Game

# Explaination -----> WAP that generates a random numnber and asks the user to guess it.
# If player's guess is lower than the actual no. the it displays "Higher No. Please", if the player's guess is higher than the actual no. then it displays "Lower No. Please", and if the user guesses it correctly then it will show the no.of guesses it takes to arrive athe correct number.

import random

print("----------The Perfect Guess Game----------")

print("-----------Are you ready? (Y/N)----------")
a = input()

if a == "Y" or a == "y" :
    counter = 0
    print("-----------lets start!!-----------")
    comp = random.randint(0,99999999999)
    print("Computer have made its choice!!")
    print("Now its your turn to guess: ")
    
    
    while ( True ):
        user_choice = int(input(f"Guess No. {counter + 1}:  "))
        if (user_choice != comp):
            counter += 1
        else:
            print(f"You took {counter + 1} guesses.")
            break

else:
    print("Come back soon!!!!")

        
