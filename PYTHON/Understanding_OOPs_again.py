# class students:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print("Init calling...")

#     def update(self):
#         self.name = "Piu"
#         self.age = 18
    
#     def compare(self, other):
#         if self.age == other.age:
#             print("Both age same")
#         else:
#             print("Both age not same")


    
# s1 = students("Ankan", 20)
# s2 = students("Shreya", 20)

# s2.update()

# print(s1.name, s1.age)
# print(s2.name, s2.age)

# s1.compare(s2)



# class cars:

#     wheels = 4

#     def __init__(self,com,type):
#         self.com = com
#         self.type = type
    
# car1 = cars("Mercedes", "Diesel")
# car2 = cars("Tesla", "Electric")

# car2.com = "Volvo"
# car2.type = "Diesel"

# cars.wheels = 8

# print(car1.com, car1.type, car1.wheels)
# print(car2.com, car2.type, car2.wheels)

# print(cars.wheels)

# class students:

#     school = "SXI"

#     def __init__(self,m1,m2,m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
    
#     def avg(self):
#         return (self.m1 + self.m2 + self.m3)/3
    
#     def get(self):
#         return self.m1
    
#     def set(self):
#         self.m1 = 100
#         return f"Value changed"
    
#     @classmethod
#     def change_school(cls):
#         cls.school = "Adamas"

#     @staticmethod
#     def add(x,y):
#         return (x+y)



# s1 = students(int(input("Enter m1 for s1: ")), int(input("Enter m2 for s1: ")), int(input("Enter m3 for s1: ")))
# s2 = students(int(input("Enter m1 for s2: ")), int(input("Enter m2 for s2: ")), int(input("Enter m3 for s2: ")))

# print(s1.get())
# print(s2.get())

# print(s1.set())
# print(s2.set())

# print(s1.avg())
# print(s2.avg())


# print(students.school)

# students.change_school()

# print(f"After changing: {students.school}")

# print(students.add(2,2))






# class students:

#     def __init__(self, name):
#         self.name = name
#         self.s_inner = self.details(19, "Kolkata", "B.Tech")
#         # self.info = self.details(19, "Kolkata", "B.Tech")
        
#     def show(self):
#         print(f"Name = {self.name}")
#         return (self.s_inner.show_details())

#     class details:

#         def __init__(self, age, city, course):
#             self.age = age
#             self.city = city
#             self.course = course
        
#         def show_details(self):
#             print(f"Age = {self.age}, City = {self.city}, Course = {self.course}")

# s_outer = students("Ankan Maity")
# s1_outer = students("Piu Paul")

# # s1_inner = students.details("20", "Kolkata", "B.Tech")

# s_outer.show()
# # s1_outer.show()






# class students:
#     def __init__(self, name, age, city, course):
#         self.name = name
#         self.s_inner = self.details(age, city, course)
        
#     def show(self):
#         print(f"Name = {self.name}")
#         self.s_inner.show_details()

#     class details:
#         def __init__(self, age, city, course):
#             self.age = age
#             self.city = city
#             self.course = course
        
#         def show_details(self):
#             print(f"Age = {self.age}, City = {self.city}, Course = {self.course}")

# s_outer = students("Ankan Maity", 19, "Kolkata", "B.Tech")
# s1_outer = students("Piu Paul", 20, "Kolkata", "B.Tech")

# s_outer.show()
# s1_outer.show()

# s_outer.s_inner.show_details()













# class outer_class:  # outer class

#     def __init__(self, name):  # __init__ of outer class
#         self.name = name
#         self.inner2 = self.inner_class(name)  # creating the object of inner class (way 2) **


#     def outer_method(self):  # method of outer class
#         print(f"{self.name} is an object of outer class")


#     class inner_class:  # inner class

#         def __init__(self, name):  # __init__ of inner class
#             self.name = name

#         def inner_method(self):  # method of inner class
#             print(f"{self.name} is an object of inner class")


# outer1 = outer_class("Outer1")  # Creating object of outer class (with parameter)
# outer1.outer_method()  # calling the method of outer class 
# outer1.inner2.inner_method() # calling the methd of inner class with the obj of outer class

# # Way 1 
# inner1 = outer_class.inner_class("Inner1")  # Creating the object of inner class [ Syntax: obj of inner class = name of outer class.name of inner class(parameter)]
# inner1.inner_method()  # calling the method of inner class








# class students:

#     def __init__(self, marks):
#         self.marks = marks

#     def __truediv__(self, another):
#         # return self.marks / another.marks
#         return "Definig what the function will do"
    
#     def __add__(self, another):
#         # return self.marks + another.marks
#         return "Definig what the function will do"

# s1 = students(100)
# s2 = students(50)

# print(s1 / s2)
# print(s1 + s2) 



import random

class Train:
    


    def __init__(self):
    
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.gender = input("Enter your gender: ")
        self.starting_loc = input("Enter starting station: ")
        self.dest_loc = input("Enter destination station: ")
        

    def book_tickets(self):
        
        trains_list = ["sealdah to belgharia",
                       "sealdah to naihati",
                       "naihati to belgharia",
                       "sealdah to belgharia",
                       "dumdum to barrackpore" ]
        counter = 0

        for i in trains_list:
            if (self.starting_loc.lower() in i) and (self.dest_loc.lower() in i):
                counter += 1
            
        seats = 500
        filled = 451

        
        if counter != 0:
            print(f"There are trains available for your route.")

            if filled < seats:
                filled += 1
                seat_no = random.randrange(filled, seats)
                print(f"Seat no. - {seat_no} is booked for {self.name}")


        else:
            print(f"There are no trains availablle for your route.")
            print("No seats left.")


temp = 1
while(temp != 0):
    P1 = Train()
    P1.book_tickets()
    print("\nThank you\n")

# P2 = Train()
# P2.book_tickets()
                
        