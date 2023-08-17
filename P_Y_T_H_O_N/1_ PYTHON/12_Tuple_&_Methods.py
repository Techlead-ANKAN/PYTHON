'''
Tuple
- once defined elemnts in the TUPLE CANNOT be ALTERED or MANIPULATED, you can ACCESS ANY VALUE.
MAJOR DIFF. - can't UPDATE ANY ELEMENT(s) OF A TUPLE
*IMPORTANT- t=(1)
            then it will print     1     - which is not a TUPLE
            but
            t=(1,)
            then it will print     (1,)   - which is TUPLE
'''

# CREATE a TUPLE using ()
t = (2, 5, 100, 450, 55)
print(t)

# EMPTY TUPLE
t = ()
print(t)

# SINGLE VALUE TUPLE
# t = (1) #WRONG way to declare a single value in a tuple. It will print the value as a no. but not a TUPLE
t = (1,) #CORRECT way to declare a single value in tuple- , is required
print(t)


# METHODS

# tuple.count() --> it will show how many times the item is used

t = (1, 5, 6, 1, 8, 5, 7, 7, 9, 8)

print(t.count(1))

# tuple.index() --> will return the position /index of the first occurence of the value

print(t.index(5))