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






class students:

    def __init__(self, name):
        self.name = name
        self.s_inner = self.details(19, "Kolkata", "B.Tech")
        # self.info = self.details(19, "Kolkata", "B.Tech")
        
    def show(self):
        print(f"Name = {self.name}")
        return (self.s_inner.show_details())

    class details:

        def __init__(self, age, city, course):
            self.age = age
            self.city = city
            self.course = course
        
        def show_details(self):
            print(f"Age = {self.age}, City = {self.city}, Course = {self.course}")

s_outer = students("Ankan Maity")
s1_outer = students("Piu Paul")

s1_inner = students.details("20", "Kolkata", "B.Tech")

s_outer.show()
s1_outer.show()


