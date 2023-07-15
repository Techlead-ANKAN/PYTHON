'''
OOPs in PYTHON
'''

# # self -- keyword used to fetch the values

# # 1) CLASS AND OBJECT--->
class computer:    # DEFINE A CLASS WITH ITS CLASS NAME
    def config(self):          #DEFINING a method name config that will show the confgiuration of the computer 
        print("Ram - 16gb\nRom - 512GB SSD")      # WHAT THE FUNCTION WILL DO
        
computer_1 = computer()    # MENTIONING  that : "computer_1" is an obect of class "computer" 

computer_1.config() # Way-1 to call the function
# Another way to call the function.
computer.config(computer_1)     # Now  i am calling the function for a particular object from the class.  SYNTAX: class_name.method_name(object_name) 

# # # SUMMARY => 
# # # 1) Defining a class with its name
# # # 2) Define a method to perform
# # # 3) now creating an object of the class 
# # # 4) call the function for a particular object in a class   TO PERFORM THE METHOD FOR A PARTICULAR OBJECT FROM THE CLASS
 

# # # 2) __init__ METHOD---> calls itself automatically & no.of times calling = no.of objects created
class initialization:
    def __init__(self,processor,ram):   # adding parameters to the method
        print("calls itself automatically. The number of times it will call is the number of objects created in the class")   
        self.processor = processor    
        self.ram = ram
    
    def config(self):
        print("config is: ", self.processor, self.ram)

# u can give arguements while creating the object by giving the arguments directly in the parenthesis()
computer_1 = initialization("Ryzen 7",16)   # this for computer 1

computer_2 = initialization("i5",8)         # this is for computer 2


# # now calling the config function
computer_1.config()
computer_2.config()


# #  Another Example of __init__ method:
class about:
    def __init__(self,standard,sec):
        self.standard = standard
        self.sec = sec
    
    def detail(self):
        print(f"Class of the student is-{self.standard} and section of the student is-{self.sec}")
    

ravi = about(11,"A")
shivam = about(9,"B")

ravi.detail()
shivam.detail()



# # 3) CONSTRUCTOR & SELF -->
# # Constructor --> This is a method that is called when an object is created. 
# #                 This method is defined in a class and can be used to initialize basic variables

# # Self --> Self represents instances/ objects of the class. This keyword can access the attributes and methods of the class. 
# #          It binds the attributes with the given arguements

class computer:
    def __init__(self):
        self.name = "Ankan"
        self.age = 18
    
    # Now i want to update the age  (Understanding SELF):
    def update(self):
        self.age = 25 
        self.age2 = 89       

p1 = computer()   # These are the Constructors   \
#                                                 >   CONSTRUCTORS   
p2 = computer()   # These are the constructros   /

p2.name= "Ravi"
p2.age2 = 19

# Now there are two oobjects where it can be many more. and u want to call the function update() for a particular object.no computer will choose random object.
# so in order to to update() a desired object you need to say object_name.fucntion().
# and for that self keyword is required.
p1.update()
p2.update()

print(p1.name)
print(p1.age)

print(p2.name)
print(p2.age2)


# # 4) COMPARING 2 OBJECTS:

class computer:
    
    def __init__(self):       #Initializing
        self.name= "ANKAN"
        self.age = 31

    def compare(self,other):        # Now i am creating a function name compare to compare there age
        if self.age==other.age:
           return True
        else:
           return False

person1 = computer()    # Creating objects
person2 = computer()    # Creating objects


person2.name = "Ravi"   # Assigning name of person2
person2.age= 30         # Assigning age of person2

# Comparing there age

if person1.compare(person2):
    print("Both of there age is same")
else:
    print("There age is differnt")




# # #5) TYPES OF VARIABLES:  (i) Class / Static variables
# # #                      (ii) Instance variables

# # #     (i) Instance variables --> these are the variables whose value changes if the object changes
class cars:

    def __init__(self):
        self.mileage = 15
        self.brand = "BMW"

car1 = cars()   # INSTANCE VARIABLES
car2 = cars()   # INSTANCE VARIABLES

car2.mileage = 9
car2.brand = "Toyota"

print(car1.mileage, car1.brand)
print(car2.mileage, car2.brand)


# #      (ii) Class/static variables --> These are the variables that remain same even if the object changes

class cars:

    wheels = 6     #--> class namespace # CLASS OR STATIC VARIABLES(define it outside the init)

    def __init__(self):
        self.mileage = 15    # Instance namespace
        self.brand = "BMW"   # Instance namespace
        

car1 = cars()
car2 = cars()

car2.mileage = 9
car2.brand = "Toyota"

cars.wheels = 8   # This is how you change a class or static variables

print(car1.mileage, car1.brand, car1.wheels)
print(car2.mileage, car2.brand, car2.wheels)



# # 6) TYPES OF METHODS-->

# # i) INSTANCE METHOD --> This method requires a self in the class. You can use this self to access any data or methods present in the class.
# #     (a) ACCESSORS  = They access the value
# #     (b) MUTATORS  = They change the value

class laptop:

    def __init__(self,price,brand,color,dis):
        self.price = price
        self.brand = brand
        self.color = color
        self.dis = dis

    def bill(self):                            # INSTANCE METHOD
        return (self.price - ((self.dis/100)*self.price))

    def fetch(self):        # ACCESSORS
        return self.color

    def change(self,correct_price):      # MUTATORS
        self.price = correct_price

cus_1 = laptop(50000,"HP","Black",5)
cus_2 = laptop(45000,"DELL","white",7)

print(f'''
Laptop for customer_1:
Brand - {cus_1.brand},
Price - {cus_1.price}/-,
color - {cus_1.color},
discount - {cus_1.dis}%,
Bill - {cus_1.bill()}/- ''')

print(f'''
Laptop for customer_2:
Brand - {cus_2.brand},
Price - {cus_2.price}/-,
color - {cus_2.color},
discount - {cus_2.dis}%,
Bill - {cus_2.bill()}/- ''')

print(f"Fetching the color of the laptop of customer 1: {cus_1.fetch()}")   # ACCESSING
cus_2.change(55000)     # MUTATING
print(f"This is the correct price for laptop of customer 2: {cus_2.price}/-")


# # ii) CLASS METHODS --> Works with class variables not instance variables. This methods are bound to class and not the objects in the class
# # A DECORATOR is required [@classmethod]
# # Instead of "self" we will use "cls"

class students:

    school = "SXI"

    def __init__(self,mark1,mark2,mark3):
        self.marks1 = mark1
        self.marks2 = mark2
        self.mark3 = mark3

    # CLASS METHOD
    @classmethod
    def change_school(cls):
        cls.school = "Adamas"

    @classmethod    # DECORATOR
    def school_name(cls):    # UsE of 'cls'
        return cls.school    
    
Ankan = students(55,48,98)
Piu = students(100,99,98)
Shreya = students(99,100,98)


# students.school = "ADAMAS"   # This is how u change value of class variable
students.change_school()

print(f"Ankan is from {Ankan.school_name()}")
print(f"piu is from {Piu.school_name()}")
print(f"Shreya is from {Shreya.school_name()}")


# # iii) STATIC METHOD --> Nothing to do with class variables or instancve variables

class students:

    school = "SXI"

    def __init__(self,mark1,mark2,mark3):
        self.marks1 = mark1
        self.marks2 = mark2
        self.mark3 = mark3

    @classmethod    
    def school_name(cls):    
        return cls.school    

    @staticmethod   # DECORATOR
    def info():         # STATIC METHOD (keep it blank since static method has got nothing to do with instance and class variables). It is a method that has no relationship with class or instance variables, it just deals with the parameters given.
        print("This is a static method...")
    
Ankan = students(55,48,98)
Shreya = students(100,99,98)
Piu = students(99,100,98)

students.school = "ADAMAS"   

print(f"Ankan is from {Ankan.school_name()}")
print(f"Shreya is from {Shreya.school_name()}")
print(f"Piu is from {Piu.school_name()}")

students.info()   # Calling Static method*


# 7) INNER CLASS - Class inside a class -->

class players:                     # OUTER CLASS

    def __init__(self,name,goals):
        self.name = name
        self.goals = goals
        self.N = self.Nation()

    def show(self):                # OUTER METHOD
        print(f"Player name- {self.name} and Goals scored- {self.goals}")   # This is what the method will do
        return self.N.show()      # This is to call the show() method of the inner class    "self.inner_class_name.method()""

    
    class Nation:                  # INNER CLASS

        def __init__(self):
            self.nation = "INDIA"
            self.age_group = "18-25"
            self.sex = "Male"
            

        def show(self):             # INNER METHOD
            print(f"Player Nation- {self.nation}, age group- {self.age_group} and sex is- {self.sex}")

p1 = players("Ankan", 25)
p2 = players("Harry",24)

p1.show()
p2.show()


# Another example for further illustration
class outer_class:  # outer class

    def __init__(self, name):  # __init__ of outer class
        self.name = name
        self.inner2 = self.inner_class(name)  # creating the object of inner class (way 2) **


    def outer_method(self):  # method of outer class
        print(f"{self.name} is an object of outer class")


    class inner_class:  # inner class

        def __init__(self, name):  # __init__ of inner class
            self.name = name

        def inner_method(self):  # method of inner class
            print(f"{self.name} is an object of inner class")


outer1 = outer_class("Outer1")  # Creating object of outer class (with parameter)
outer1.outer_method()  # calling the method of outer class 
outer1.inner2.inner_method() # calling the methd of inner class with the obj of outer class

# Way 1 
inner1 = outer_class.inner_class("Inner1")  # Creating the object of inner class [ Syntax: obj of inner class = name of outer class.name of inner class(parameter)]
inner1.inner_method()  # calling the method of inner class




# 8) INHERITANCE
#  i) Single
#  ii) Multi-Level
#  iii) Multiple

# i) Single Inheritance

class A:

    def feature_1(self):
        print("Feature 1 working")

    def feature_2(self):
        print("Feature 2 working")

class B(A):    # ---> SINGLE INHERITANCE [Syntax: <Inheriting_class> (<Inherited_class>)]

    def feature_3(self):
        print("Feature 3 working")
    
    def feature_4(self):
        print("Feature 4 working")

obj = B() # creating object of B
# obj1 = A()
# Note : class A cannot acces the method of class B

obj.feature_1() # method of A
obj.feature_2() # method of A
obj.feature_3() # method of B
obj.feature_4() # method of B

# obj1.feature_3() # AttributeError: 'A' object has no attribute 'feature_3'.


# ii) Multi-Level Inheritance

class A:

    def feature_1(self):
        print("Feature 1 working")

    def feature_2(self):
        print("Feature 2 working")

class B(A):          # ---> SINGLE INHERITANCE

    def feature_3(self):
        print("Feature 3 working")
    
    def feature_4(self):
        print("Feature 4 working")

class C(B):          # MULTI-LEVEL INHERITANCE
    def feature_5(self):
        print("Feature 5 working")

    def feature_6(self):
        print("Feature 6 working")


obj = C()

obj.feature_1()
obj.feature_2()
obj.feature_3()
obj.feature_4()
obj.feature_5()
obj.feature_6()


# iii) Multiple Inheritance


class A:

    def feature_1(self):
        print("Feature 1 working")

    def feature_2(self):
        print("Feature 2 working")

class B:         

    def feature_3(self):
        print("Feature 3 working")
    
    def feature_4(self):
        print("Feature 4 working")

class C(A,B):          # MULTIPLE INHERITANCE
    def feature_5(self):
        print("Feature 5 working")

    def feature_6(self):
        print("Feature 6 working")

obj = C()

obj.feature_1()
obj.feature_2()
obj.feature_3()
obj.feature_4()
obj.feature_5()
obj.feature_6()


#  9) CONSTRUCTOR IN INHERITANCE-->
#  A- super class, B- sub class

class A:
    def __init__(self):
        print("Class A init")

    def feature_1(self):
        print("feature 1-A")
    

class B(A):
    def __init__(self):
        print("Class B init")

    def feature_2(self):
        print("Feature B-2")

obj = B()        
# Will B call its init or A's init---Yes it will call B's init, if B do not have its own init then it will go for init of super class


# 10) super()-->
# A - Super class, B - Super class, C - Sub class

class A:
    def __init__(self):
        print("Class A init")

    def feature_1(self):
        print("feature 1-A")

class B:
    def __init__(self):
        print("Class B init")

    def feature_2(self):
        print("Feature B-2")

class C(A,B):

    def __init__(self):
        super().__init__()
        print("Class C init")
    
    def feature_3(self):
        print("Feature 3-C")

# What will happen now? will it call for A or B or for both A and B         
obj = C()     


# METHOD RESOLUTION ORDER(MRO)--> LEFT TO RIGHT
class A:
    def __init__(self):
        print("Class A init")

    def feature_1(self):
        print("feature 1-A")
    

class B:
    def __init__(self):
        print("Class B init")

    def feature_2(self):
        print("Feature B-2")

class C(B,A):

    def __init__(self):
        super().__init__()
        print("Class C init")
    
    def feature_3(self):
        print("Feature 3-C")

obj = C()   
# Now which init will it call.
# The order of calling is from left to right.
# Suppose c(a,b)
# then it will call 'a' then 'c'
# Suppose c(b,a)
# Then it will call 'b' then 'c'



# 11) POLYMORPHISM--> Objects will have multiple forms

# Types of Polymorphism - 1) DUCK TYPING, 2) OPERATOR OVERLOADING, 3) METHOD OVERLOADING, 4) METHOD OVERWRITTING


# 11.1) DUCK TYPING---> "if a bird that walks like a duck, swims like a duck, quacks like a duck, flies like a duck, then it is a duck"

class vscode:                 # Here the vscode is the DUCK

    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:

    def execute(self):
        print("Spell check")
        print("Indentation check")
        print("Compliling")
        print("Running")
        print("Executing")

class programs:

    def code(self,ide):      # Here the ide is the BIRD
        ide.execute()        # execute is a fucntion that will execute the code in the selected ide.

ide = MyEditor()        # Declaring that the ide will be of myeditor type
                      # story_wise the bird is a duck

obj = programs()

obj.code(ide)   # Now calling "code" method of class "programs" where the parameter is "ide" (THE BIRD) which is of type "vscode" (THE DUCK)


# **MAGIC METHODS--> __add__(), __sub__(), __mul__(),....etc.
a = 4
b = 5
str1 = "AN"
str2 = "KAN"
print(a+b) # u call this
print(int.__add__(a,b))  # this is what happens behind the scenes
print(str1 + str2)
print(str.__add__(str1,str2))



# 11.2) OPERATOR OVERLOADING-->
class student:
    
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
       
    def __add__(self,others):
        m1 = self.m1 + others.m1
        m2 = self.m2 + others.m2

        res = student(m1,m2)
        return res
        

    def __gt__(self,others):
        r1 = self.m1 + self.m2
        r2 = others.m1 + others.m2

        if r1 > r2:
            return True 
        else:
            return False
 
s1 = student(2,7)        
s2 = student(4,3) 
s3 = student(5,8) 
     # (PHYSICS,MATHS) MARKS (let)


s4 = s1+s2       # THIS IS THE FUNC NAME res THAT WILL DO THE WORK AS PER WE DO THE WORKS IN __add__ method
print(s4)
print(s4.m1)
print(s4.m2)


if s1>s2:
    print("S1 Wins")
else:
    print("S2 Wins")


# Another example: -
class students:

    def __init__(self, marks):
        self.marks = marks

    def __truediv__(self, another):
        # return self.marks / another.marks
        return "Defining what the function will do"
    
    def __add__(self, another):
        # return self.marks + another.marks
        return "Definig what the function will do"

s1 = students(100)
s2 = students(50)

print(s1 / s2)
print(s1 + s2)

# Mapping Operators to functions: - [ Link:  https://docs.python.org/3/library/operator.html#:~:text=Mapping%20Operators%20to,gt(a%2C%20b) ]




# 11.3) Method Overloading


