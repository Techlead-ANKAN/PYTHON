# Heads or Tails

import random

choices = ["heads", "tails"]

while (True):
    dup = ["heads", "tails"]

    no = random.randint(0,2)
    if no == 1:
        print("Computer gets to choose first.\n")
        comp = random.choice(choices)
        print(f"Computer's choice: {comp}\n")
        dup.remove(comp)
        you = dup[0]
        print(f"Your Choice: {you}\n")
        coin = random.choice(choices)
        print(f"Coin Shows: {coin}\n")

        if coin == "heads":
            if comp == coin:
                print("Computer Wins!!")
                break
            else:
                print("You win!!!")
                break

        elif coin == "tails":
            if comp == coin:
                print("computer Win!!!")
                break    
            else:
                print("You Win!!!")
                break

    elif no == 2:
        print("Player gets to choose first.\n")
        you = input("Enter your choice (Heads/Tails): ")
        if you.lower() == "head":
            dup.remove("heads")
        else:
            dup.remove("tails")
        comp = dup[0]
        print(f"Computer's choice: {comp}\n")
        
        coin = random.choice(choices)
        print(f"Coin Shows: {coin}\n")

        if coin == "heads":
            if comp == coin:
                print("Computer Wins!!")
                break
            elif you.lower() == coin or you.lower() == "head":
                print("You win!!!")
                break

        elif coin == "tails":
            if comp == coin:
                print("computer Win!!!")
                break    
            elif you.lower() == coin or you.lower() == "tail":
                print("You Win!!!")
                break
    

    




