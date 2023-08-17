'''
IF-ELIF-ELSE
Syntax:
if (condition 1):
    print("IF CONDITION 1 IS TRUE THEN PRINT: YES")              
elif (condition 2)
    print("IF CONDITION 2 IS TRUE THEN PRINT: YES")
else:
    pirnt("IF BOTH THE CONDITIONS ARE FALSE THE PRINT: NO")

'''

# If-Elif-Else ladder

# Case: 1 [When the FIRST condition (or if condition) is true]
a =20
if (a>5):
    print("The value of a is greater than 5")     
elif(a<50):
    print("The value of a is less than 50")
elif (a==20):
    print("The value of a is equals to 20")
else:
    print("The conditions are incorrect")    # RESULT = The value of a is greater than 5


# Case: 2  [When the FIRST condition is not true but any of the ELIF condition is true then it will run the "print" under that condition ]
a =2
if (a>5):
    print("The value of a is greater than 5")     
elif(a<50):
    print("The value of a is less than 50")
elif (a==20):
    print("The value of a is equals to 20")
else:
    print("The conditions are incorrect")   # RESULT = The value of a is less than 50


# Case: 3  [When FIRST(if) condition is false and suppose there are two other (elif) conditions and both of them are correct the it will run the first condition among the two ]
a =2
if (a>5):
    print("The value of a is greater than 5")     
elif(a<50):
    print("The value of a is less than 50")
elif (a==2):
    print("The value of a is equals to 2")
else:
    print("The conditions are incorrect")  # RESULT = "The value of a is less than 50"


# Case: 4  [when all the conditions ( if, elif) are true then it will run the FIRSTcondition that is the, if condition]
a =2
if (a>1):
    print("The value of a is greater than 1")     
elif(a<50):
    print("The value of a is less than 50")
elif (a==2):
    print("The value of a is equals to 2")
else:
    print("The conditions are incorrect")  # RESULT = "The value of a is greater than 1"


# Case: 5  [when all the conditions ( if, elif) are FALSE then it will run the LAST  condition that is the,  else  condition]
a =25
if (a>100):
    print("The value of a is greater than 100")     
elif(a<5):
    print("The value of a is less than 5")
elif (a==20):
    print("The value of a is equals to 20")
else:
    print("The conditions are incorrect")   # RESULT = "The conditions are incorrect "



# Q-1 W.A.P to print "Yes" when the age entered by the user is greater than or equals to 18

age = int(input("Enter your age: "))

if (age>=18):
    print("Yes")
else:
    print("No")

    