'''
PRACTICE SET-4_
'''

# Question-1
# Store seven FRUITS in a list entered by the user

f1 = input("Enter Fruit number 1: ")
f2 = input("Enter Fruit number 2: ")
f3 = input("Enter Fruit number 3: ")
f4 = input("Enter Fruit number 4: ")
f5 = input("Enter Fruit number 5: ")
f6 = input("Enter Fruit number 6: ")
f7 = input("Enter Fruit number 7: ")

listoffruits = [f1, f2, f3, f4, f5, f6, f7]
print(listoffruits)

# Question-2
# To accept marks of 6 students and display them in a sorted manner

m1 = int(input("Enter marks of student one: "))
m2 = int(input("Enter marks of student two: "))
m3 = int(input("Enter marks of student three: "))
m4 = int(input("Enter marks of student four: "))
m5 = int(input("Enter marks of student five: "))
m6 = int(input("Enter marks of student six: "))

marklist = [m1, m2, m3, m4, m5, m6]
marklist.sort()
print(marklist)

# Question-3
# Check that a tuple cannot change in python

t = (1, 56, 84, 72)
t[1] = 44
print(t) # It show error that 'tuple' object does not support item assignment

# Question-4
# A list with 4 numbers. SUM the items of the list

l = [2, 5, 8, 9]
print(l[0] + l[1] + l[2] + l[3])

# Question-5
# Count no.of zeros in a following TUPLE

a = (7, 0, 8, 0, 0, 9)
print(a.count(0))

