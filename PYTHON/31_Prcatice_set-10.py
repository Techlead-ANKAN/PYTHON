'''
Practice Set- 10
'''

# 1) Create a class programmer to store information of few programmers working at Microsoft

# way 1
class programmer:

    def __init__(self,name,age,designation):
        self.name = name
        self.age = age
        self.designation = designation

    def about(self):
        print(f"{self.name} works at Microsoft, whose age is {self.age} and designation is {self.designation}")

e1 = programmer("Ankan Maity", 24, "Software Developer")
e2 = programmer("Piu Paul", 24, "Software Developer")
e3 = programmer("Harry", 24, "Software Enginner")

e1.about()
e2.about()
e3.about()

# way 2
class programmer :
    
    def __init__(self, name, age, city, phone_no, gender):
        self.name = name
        self.pd = self.programmer_details(age, city, phone_no, gender)
        
        
    def show(self):
        print(f"Name - {self.name}")
        self.pd.details()
        
        
    
    class programmer_details:

        def __init__(self,age, city, phone_no, gender):
            self.age = age
            self.city = city
            self.phone_no = phone_no
            self.gender = gender


        def details(self):
            print(f"Age - {self.age}\nCity - {self.city}\nPhone No. - {self.phone_no}\nGender - {self.gender}\n\n")


E1 = programmer("Ankan Maity", 24, "Kolkata", 8617790081, "Male")
E2 = programmer("Piu", 23, "Kolkata", 7029488160, "Female")

E1.show()
E2.show()



# 2) Write a class calculator which is capable of finding square, cube and square root of a number.

# class calculator:

#     def __init__(self):
#         self.number = float(input("Enter a number: "))

#     def calculate(self):
#         print(f"Square of {self.number}= {self.number**2},\nCube of {self.number}= {self.number**3},\nSquare root of {self.number} = {self.number**(0.5)}")


# n1 = calculator()
# n1.calculate()



# 3) Create a class with a class attribute "a", create an object from it and set 
# a directly using object a = 0. Does this change the class attribute?

# class sample:
#     a = "Ankan"

# obj = sample()
# obj.a = "Piu"

# print(obj.a)

# print(sample.a)



# 4) Add a static method in Question-2 to greet the user with "Hello".

# class calculator:

#     @staticmethod
#     def greet():
#         print("Hello")

#     def __init__(self):
#         self.number = float(input("Enter a number: "))

#     def calculate(self):
#         print(f"Square of {self.number}= {self.number**2},\nCube of {self.number}= {self.number**3},\nSquare root of {self.number} = {self.number**(0.5)}")


# n1 = calculator()
# calculator.greet()
# n1.calculate()



# 5) Write a class Train which has methods to book a ticket, get status (no.of seats) and get fare information of trains running under Indian Railways.


# class Train:
        
#     seats = 125
#     filled = 85
#     fare = "255/-"

#     def tourist(self):
#         self.name = input("Enter tourist name: ")
#         self.age = int(input("Enter age: "))
#         self.destination = input("Enter destination: ")
#         self.start = input("Enter starting location: ")
#         self.date = input("Enter date: ")

#     def book(self):
#         print(f"Tickect Booked: \nName: {self.name}\nAge: {self.age}\nDestination: {self.destination}\nStarting from: {self.start}\nDate: {self.date}")

#     @classmethod
#     def get_status(cls):
#         print(f"Total Seats: {Train.seats}\nOccupied Seats: {Train.filled}\nVacant Seats: {Train.seats - Train.filled}")

#     @classmethod
#     def get_fare(cls):
#         print(f"Fare for the ticket: {Train.fare}")

# t1 = Train()

# t1.tourist()
# t1.book()
# Train.get_status()
# Train.get_fare()



# 6) Can you change the "self" parameter inside the class to something else (say "Ankan"). 
# Try changing "self" to "slf" or "Ankan" and see the effects.

# class sample:
#     def __init__(slf,name):
#         slf.name = name

# obj = sample("Ankan")

# print(obj.name)
