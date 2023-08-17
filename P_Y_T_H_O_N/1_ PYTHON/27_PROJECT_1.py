import random

def winner(comp, you):

    if comp == you:
        return None

    elif comp=="rock":
        if you == "paper":
            return True
        elif you == "scissor": 
            return False

    elif comp == "paper":
        if you == "rock":
            return False
        elif you == "scissor":
            return True

    elif comp == "scissor":
        if you == "rock":
            return True
        elif you == "paper":
            return False

print(" Computer decided its move ")
rand = random.randint(1,3)
comp = ""
if rand == 1:
 comp = "rock"
elif rand == 2:
    comp = "paper"
elif rand == 3:
    comp = "scissor"

you = input("Your Turn: rock, paper or  scissor: ")
a = winner(comp, you)

print("Computer chose:",comp)
print(f"You chose: {you}")

if a == None:
    print("The game is Tie")
elif a == True:
    print("You Won")
else:
    print("You lose")
    