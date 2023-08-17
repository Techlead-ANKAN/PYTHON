'''
Practice set-7
'''

# 1) wap to print multiplication table of a given num using for loop
num = int(input("Enter any number to show its multiplication table: "))

for i in range(1,11):
    print(str(num) + " X" + " str(i)" + " = " + str(num*i))


# 2) wap to greet all person  whose name is starting with "s" in the sorted list.
# list = ["Harry", "Soham", "Sachin", "Rahul"]

# for name in list:
#     if name.startswith("S"):
#      print("Good Morning ",name)
 


# 3) wap to print multiplication table of a given num using for loop
# num = int(input("Enter any number to show its multiplication table: "))
# i = 1
# while i<=10:
#     print(num*i)
#     i = i+1


# 4) wap to find whether a given number is prime or not.
# num = int(input("Enter a number: "))
# prime = True                                # We are considering that the no. is prime 
# for i in range(2, num):
#     if (num%i==0):                        # if the number is divided by the numbers between (2 to number itself)      
#       prime = False                                  # any number between 1 to number itself divides the number then it is not a prime no.
#       break                                   # breaks the condition when the condition matches
                                  
# if prime:
#  print("The no is prime")
# else:
#  print("The no. is not prime")



# 5) wap to print the sum of first n natural numbers using while loop

# n = int(input("Enter a number: "))

# if n<0:
#     print("Please enter a positive integer")
# else:
#     sum = 0

#     while n>0:
#         sum = sum + n
#         n = n- 1
#     print("The result is ",sum)



# 6) wap to calculate factorial of a given number using for loop
# num = int(input("Enter a number: "))

# factorial = 1

# for i in range (1, num+1):
#     factorial = factorial*i
#     print(f"factorial of {num} is {factorial}")



# 7) print star pattern
#    *
#   ***
#  *****     for n=3

# n = 3
# for i in range(3):
#     print(" " * (n-i-1), end="")
#     print("*"*(2*i+1),  end="")
#     print(" "* (n-i-1))



# 8) print star pattern
# *
# **
# ***

# n = 4
# for i in range(4):
#     print("*" * i)



# 10) wap to print multiplication table of a given num using for loop in reversed order
# num = int(input("Enter any number to show its multiplication table: "))

# for i in range(10,0,-1):
#     print(str(num) + " X" + " str(i)" + " = " + str(num*i))


