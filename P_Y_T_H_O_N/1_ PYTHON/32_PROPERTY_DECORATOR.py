# property decorator in python [ @property ] -- It is a built-in decorator in python that is helpful in defining the properties effortlessly.

# Example: -
# Suppose you want to build a program where you want to calculate the total salary based on the base salary and salary bonus


class employee:

    E_name = input("Enter name: ")
    salary = int(input("Enter base salary: "))
    salary_bonus = 2000

    # Now suppose I want to calculate the total salary on the basis of salary bonus and salary

    # way 1 (hard code)      [ Not right ]
    # total_salary = 80000 


    # way 2 ( using @property )     Note - method name with property decorator is also known as getters

    @property
    def total_salary(self):  #it is a function but will be appeared as a property                          
        # now it is not hard codded if there is any chnage in salary or salary bonus it will be reflected in the total salary
        print(self.salary + self.salary_bonus)


E1 = employee()

E1.total_salary       # we generally call the function with parenthesis but "total_salary" is like a property now.




# Example 2

class annual_exam:

    def __init__(self):
        self.name = input("Enter your name: ")
        self.Class = input("Enter your standard: ")
        self.sec = input("Enter section: ")
        self.roll_no = int(input("Enter your roll_no: "))
        self.PHY_marks = int(input("Enter marks in Physics: "))
        self.MATHS_marks = int(input("Enter marks in Maths: "))
        self.CHEM_marks = int(input("Enter marks in Chemistry: "))


    @property              # decorator
    def results(self):
        res = self.CHEM_marks + self.MATHS_marks + self.PHY_marks

        if res >= 140:
            print("Pass")
        else:
            print("Fail")
        

S1 = annual_exam()

print(S1.results)



# setters

# Syntax:   
# @method_name(in property decorator).setter
# def method_name(self, val):
#   self.something = val



class laptop:

    def __init__(self, name, color, brand):
        self.name = name
        self.color = color
        self.brand = brand 

    
    @property              # getter (property decorator)
    def details(self):
        print(f"Laptop name - {self.name}, Brand - {self.brand}, Color - {self.color}")

    @details.setter         # Setter
    def details(self, val):
        self.color = val

    

l1 = laptop("Katana GF66", "Black", "MSI")
l1.details


l1.details = "Red"
l1.details