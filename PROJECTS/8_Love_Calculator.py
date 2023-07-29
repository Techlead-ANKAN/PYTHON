# Love Calculator
import random
class love:

    def __init__(self):
        self.your_name = input("Enter your name: ")
        self.partner_name = input("Enter your partner name: ")
    
    def love_calculator(self):
        self.your_age = int(input("Enter your age: "))
        self.partner_age = int(input("Enter your partner age: "))
        flag = 0

        if self.your_age > self.partner_age:
            if (self.your_age - self.partner_age) <= 7:
                age_diff = self.your_age - self.partner_age
                flag = 1
            elif (self.your_age - self.partner_age) > 7:
                flag = 0
        
        elif self.your_age < self.partner_age:
            if (self.partner_age - self.your_age) <= 7:
                age_diff = self.partner_age - self.your_age
                flag = 2
            elif (self.partner_age - self.your_age) > 7:
                flag = 0
        
        else:
            age_diff = 0
            flag = 3


        if flag == 1 or flag == 2 or flag == 3:
            print(f"Love b/w {self.your_name} and {self.partner_name} ----> {random.randint(1, 101)}")
        else:
            print(f"Love b/w {self.your_name} and {self.partner_name} ----> {random.randint(1, 101)}")

ob = love()

ob.love_calculator()
