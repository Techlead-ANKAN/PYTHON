'''
FUNCTIONS - These are a set of codes that are written once and can be used in any part of the program by calling it with the function name.
'''

# Example 1:

def avg(a,b):
    return((a+b)/2)

a = 25
b = 15
average = avg(a,b)
print(average)


# Example-2:
def percent(marks):
    return((sum(marks))/500)*100

marks = [95, 65, 88, 57, 91]
print(percent(marks))


# Quick Quiz
# Q) wap to greet a user with "Good Day" using function
def greet(user):
    return("Good Day " + user)

user = input("Enter user name: ")
print(greet(user))

# # Q) 
def tempex(T,unit):
    
    if unit[-1]=="C":
        Tf = int((T/5)+(32/9))
        return("Converted from Celsius to Fahrenheit: ",Tf )
    elif unit[-1]=="F":
        Tc = int((T-(32/9))/5)
        return("Converted from Fahrenheit to Celsius: ",Tc )
        
T = int(input("Enter temperature to convert: "))
unit = input("Enter the unit of the temp. given: ")
print(tempex(T,unit))



# DEFAULT PARAMETER VALUE

# Example 1:
# def greet(user):
#     return("Good Day " + user)

# user = input("Enter user name: ")
# print(greet(user))


def greet(user = "Stranger"):                # now this is called DEFAULT PARAMETER VALUE 
    return("Good Day " + user)


user = input("Enter user name: ")
print(greet())             # now aas u can see no arguement(name) is given so i want the it to show "Good Day stranger"
