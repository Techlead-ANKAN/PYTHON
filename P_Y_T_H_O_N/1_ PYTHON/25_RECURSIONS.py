'''
RECURSION- it is the process of calling a function inside the same function
'''

# n! = 1*2*3*4....*(n-1)*n
# which means we can wirte formula of factorial => n! = (n-1)!*n


def factorial(n):
    if (n==1 or n==0):
        return 1
    else:
        return (n * factorial(n-1))  # See i am calling the function "factorial()" inside the function "factorial()"

a = int(input("Enter a number: "))
print(factorial(a))


# Area of a triangle

a = float(input("Enter first side of a triangle: "))
b = float(input("Enter second side of a triangle: "))
c = float(input("Enter third side of a triangle: "))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print(str(area))



# Quadratic eqn.
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
dis = ((b**2) - (4*a*c)) ** 0.5

quad1 = (-b + dis)/ (2*a)
quad2 = (-b - dis)/ (2*a)

print(f"Answers: {quad1},{quad2}")
