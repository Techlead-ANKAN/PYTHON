'''
Type casting - Process of changing a Data Type to another Data Type.
'''
a = "2000" # it is a String Data Type 
a = int(a)  # line converting Data type(String to Int:" here") 
print(type(a))
print(a + 500)

# Int to String
b = 5
b = str(5)
print(type(b))

# String to Int
c = "100"
c = int(c)
print(type(c))

# Int to Float
d = 55
d = float(d)
print(type(d))

# String to Float
e = '959'
e = float(e)
print(type(e))
print( e + 22.0)



'''
About "input()" function
'''

a = input(" Enter your name: ")
print(a)
print(type(a))


a = input(" Enter a number: ")
print(a)
print(type(a))


'''
Type Casting & input() function in one program
'''

a = input("Enter a no. ")
a = int(a) # Converts data types( if possible ) eg: a name cannot be converted into a int or float data type
print(type(a))