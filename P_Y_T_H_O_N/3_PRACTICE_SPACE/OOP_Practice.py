# OOPs Practice  

# 1. Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

class Circle:

    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        print(f"Area of circle = {(22/7) * (self.radius**2)}")

    def perimeter(self):
        print(f"Perimeter of Circle = {2 * (22/7) * self.radius}")

c1 = Circle(4)

c1.area()
c1.perimeter()


# 2. Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.

from datetime import date

class person:

    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob

    def cal_age(self):
        today = date.today()
        age = today.year - self.dob.year

        if today < date(self.dob.year, self.dob.month, self.dob.day):
            print("Invalid Date of Birth!")
        else:
            print(f"{self.name}'s Age = {age}")

p1 = person("Ankan Maity", "India", date(2003, 5, 19))
p2 = person("Piu Paul", "India", date(2004, 12, 2))

p1.cal_age()
p2.cal_age()


# 3. Write a Python program to create a calculator class. Include methods for basic arithmetic operations.

class details:

    def __init__(self):
        self.a = float(input("Enter 1st Operand: "))
        self.b = float(input("Enter 2nd Operand: "))
        print("1 --->  Addition\n2 --->  Subtraction\n3 --->  Multiplication\n4 --->  Quotient\n5 --->  Remainder")
        self.op = int(input("Enter operator: "))

class operations(details):

    def __add__(self):
        print(f"Result: {self.a} + {self.b} = {self.a + self.b}")

    def __sub__(self):
        print(f"Result: {self.a} - {self.b} = {self.a - self.b}")
    
    def __mul__(self):
        print(f"Result: {self.a} * {self.b} = {self.a * self.b}")

    def __truediv__(self):
        print(f"Result: {self.a} / {self.b} = {self.a / self.b}")

    def __mod__(self):
        print(f"Result: {self.a} % {self.b} = {self.a % self.b}")

class calculator(operations):

    def calculate(self):

        if self.op == 1:
            self.__add__()
        
        elif self.op == 2:
            self.__sub__()
        
        elif self.op == 3:
            self.__mul__()
        
        elif self.op == 4:
            self.__truediv__()
        
        elif self.op == 5:
            self.__mod__()

        else:
            print("Invalid Operator")


ob = calculator()
ob.calculate()



# 4. Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.

class circle:

    def __init__(self):
        self.radius = float(input("Enter radius of circle: "))

    def circle_area_perimeter(self):
        print(f"Area of Circle = {(22/7) * (self.radius**2)}\nPerimeter of Circle = {2 * (22/7) * self.radius}")

class triangle:

    def __init__(self):
        self.a = float(input("Enter 1st side of triangle: "))
        self.b = float(input("Enter 2nd side of triangle: "))
        self.c = float(input("Enter 3rd side of triangle: "))

    def triangle_area_perimeter(self):
        s = (self.a + self.b + self.c) / 2
        print(f"Area of Triangle = {(s*(s-self.a)*(s-self.b)*(s-self.c))**0.5}\nPerimter of Triangle = {self.a + self.b +self.c}")

class square:

    def __init__(self):
        self.s = float(input("Enter side of square: "))

    def square_area_perimeter(self):
        print(f"Area of Square = {self.s**2}\nPerimeter of Square = {4*self.s}")

class rectangle:

    def __init__(self):
        self.length = float(input("Enter length of rectangle: "))
        self.breadth = float(input("Enter breadth of rectangle: "))

    def rectangle_area_perimeter(self):
        print(f"Area of Rectangle = {self.length * self.breadth}\nPerimeter of Rectangle = {2 * (self.breadth + self.length)}")

print("1 --->  Circle\n2 --->  Triangle\n3 --->  Square\n4 --->  Rectangle\n")
shape_choice = int(input("Enter Shape: "))

if shape_choice == 1:
    class shape(circle):
        pass

elif shape_choice == 2:
    class shape(triangle):
        pass

elif shape_choice == 3:
    class shape(square):
        pass

elif shape_choice == 4:
    class shape(rectangle):
        pass
else:
    print("Invalid Input!")

ob = shape()
ob.circle_area_perimeter()


# 5. Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.


# 6. Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.


# 7. Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting and deleting nodes.


# 8. Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.


# 9. Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping and displaying elements.


# 10. Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.


# 11. Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.