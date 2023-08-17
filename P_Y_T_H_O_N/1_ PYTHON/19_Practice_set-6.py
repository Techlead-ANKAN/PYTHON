# '''
# PRACTICE SET - 6
# '''

# # 1) wap to find the greatest of 4 no.s entered by the user.

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# d = int(input("Enter fourth number: "))

# if (a>b) and (a>c) and (a>d):
#     print("a is the greatest")
# elif (b>a) and (b>c) and (b>d):
#     print("b is the greatest")
# elif (c>a) and (c>b) and (c>d):
#     print("c is the greatest")
# else: 
#     print("d is the greatest")


# # 2) wap to find out if a student is PASS or FAIL , if it requires TOTAL-40% and atleast 33% in each subject.Assume the marks of 3 subjects entered by the user.

# m1 = int(input("Enter marks of Physics: "))
# m2 = int(input("Enter marks of Computer: "))
# m3 = int(input("Enter marks of Maths: "))

# fm = 100   # FULL MARKS IN EACH SUBJECT
# tm = 300   # TOTAL MARKS OF 3 SUBJECTS

# M = m1+m2+m3   # TOTAL MARKS OBTAINED BY THE STUDENT
# print("Total Marks obtained: ",M)   

# p1 = (m1/fm)*100  # PERCENTAGE IN PHYSICS
# p2 = (m2/fm)*100  # PERCENTAGE IN COMPUTER
# p3 = (m3/fm)*100  # PERCENTAGE IN MATHS

# P = (M/tm)*100   # TOTAL PERCENTAGE
# print("Total Percentage obtained: ",P)  

# if (p1>=33) and (p2>=33) and (p3>=33) and (P>=40): 
#     print("The student has PASSED")
# else:
#     print("The student has FAILED")


# # 3)  A spam comment is defined if it contains these keywords : "makes a lot of maoney" , "buy now" , "subscribe this" , "click this".
# # Now wap to to detect these spams.

# spam1 = ("makes a lot of money")
# spam2 = ("buy now")
# spam3 = ("subscribe now")
# spam4 = ("click this")

# str = input("Enter any text: ")

# if (spam1 in str):
#     print("SPAM DETECTED")
# elif (spam2 in str):
#     print("SPAM DETECTED")
# elif (spam3 in str):
#     print("SPAM DETECTED")
# elif (spam4 in str):
#     print("SPAM DETECTED")
# else:
#     print("NO SPAM DETECTED")


# # 4)
# name = input("Enter your name: ")
# L = len(name)

# if (L<10):
#     print("Less than 10 characters")
# else:
#     print("More than 10 characters")   


# # 5)
# list = ["ANKAN", "HARRY", "SHREYA"]
# a = input("enter a name: ")

# if (a in list):
#     print("Name is present")
# else:
#     print("Name is not present")


# # 6)
# marks = int(input("Enter students marks: "))

# if (marks>90) and (marks<=100):
#     print("REMARKS- EXCELLENT")
# elif (marks>80) and (marks<=90):
#     print("GRADE- A")
# elif (marks>70) and (marks<=80):
#     print("GRADE- B")
# elif (marks>60) and (marks<=70):
#     print("GRADE-C")
# elif (marks>50) and (marks<=60):
#     print("GRADE-D")
# else:
#     print("GRADE-F")


# 7)
post = input("Enter any post: ")
name = "Harry"

if (name in post):
    print("Post is about Harry")
else:
    print("Post is not about Harry")




