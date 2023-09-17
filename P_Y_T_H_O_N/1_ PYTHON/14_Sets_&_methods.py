'''
SETS =  it is a collection of non repeatative elements
'''
# CREATING A SET
a ={1, 2, 3, 1}   # It will not print any repeatative items
print(type(a))
print(a)

# CREATING AN EMPTY SET              
b = set()
print(b)
print(type(b))


'''
SET METHODS
'''

# ADDING values to a set
c = {1, 2, 3}
print(type(c))
c.add(4)
c.add(5)
#  c.add([6, 7])   you cannot add list to a set
# c.add({9:8})   you cannot add dictionary to a set

c.add((10, 25, 35))  # you can add tuple to a set
print(c)  

print(len(c))# Finding the no.of elements in the set

# REMOVING an element from a set
c.remove(5)
print(c)

# set.pop() -- it removes the element and returns the value
print(c.pop())


# set.clear()  -- empties the set
print(c.clear())

# set.union() -- returns a new set with all the values of both the sets
a1 = {1, 2, 3}
a2 = {4, 5, 6}
print(a1.union(a2))

# set.intersection() -- returns a new set of the common values present in both the set
a3 = {1, 2 , 3}
a4 = {2, 3 , 4}
print(a3.intersection(a4))