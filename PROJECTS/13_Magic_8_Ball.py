#  Magic 8 Ball

import random
import time


print("-----Magic 8 Ball-----\n")
name = input("What is your name? ")
print(f"Hi {name}\n")

fortunes = ["It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely",
               "You may rely on it", "As I see it, yes", "Most Likely", "Outlook Good",
               "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later",
               "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
               "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very Doubtful"]

while(True):

    a = input("Do you have any questions? ")
    if a.lower() == 'yes':     
        question = input("Ask any question: ")
        sleep_time = time.sleep(random.randint(0, 10))
        print("Let Magic 8 Ball think.\n")
        answer = random.choice(fortunes)
        print(answer)
    else:
        print("Thank you.")



