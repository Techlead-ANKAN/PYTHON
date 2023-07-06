#      For loops - this is used to iterate through a sequence like list, tuple or string[iterables]



#Example-1
fruits = ["Mangoes", "Apple", "Guava", "Orange"]
for items in fruits:
    print(items)


# range(star,stop,step size) function

# Basic 
#1)
for i in range(4,8):
    print(i)

# 2) 
for i in range(0,10,2):
    print(i)



'''
for loop with else - > an optional else is used with afor loop if the code is to be executed when the loop exhausts
'''



for i in range(0,20,1):
    print("condition is true ",i)
else:
    print("will print when the condition is exhausted ")