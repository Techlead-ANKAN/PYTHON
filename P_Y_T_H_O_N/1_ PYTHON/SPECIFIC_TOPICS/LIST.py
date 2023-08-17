'''
LIST - []
'''

list = [1,2,3,4,5,6]
list2 = ["ANKAN", 18, 2003, 2022]
list3 = [2,89,54,78,6,1]

# UPDATE LIST

list[1] = 99
print(list)


# DELETING LIST  -  (del statement)
del list[4]
print(list)


# BASIC LIST OPERATIONS
# 1. length
print(len(list))

# 2. Concatenation
print(list+list2)

# 3. Repetition
print(list*4)


# 4. Membership
if 3 in list:
    print("Present")
else:
    print("Not Present")


# Iteration
for n in list:
    print(n)

'''
LIST METHODS
'''

# Method	           Description

# 1. append()	Adds an element at the end of the list
list.append(99)
print(list)


# 2. clear()	Removes all the elements from the list
list.clear()
print(list)


# 3. copy()	    Returns a copy of the list
copied_list = list.copy()
print(copied_list)


# 4. count()	Returns the number of elements with the specified value
counter = list.count(1)
print(counter)


# 5.  extend()	Add the elements of a list (or any iterable), to the end of the current list
list.extend(list2)
print(list)


# 6.  index()	Returns the index of the first element with the specified value
res = list3.index(2)
print(res)


# 7. insert()	Adds an element at the specified position
list.insert(2,3)
print(list)


# 8. pop()	Removes the element at the specified position
a = list.pop(3)
print(a)


# 9. remove()	Removes the first item with the specified value
list.remove(3)
print(list)


# 10. reverse()	    Reverses the order of the list
list.reverse()
print(list)

# 11. sort()	Sorts the list
list3.sort()
print(list3)


#  max()     Finds the biggest value from the list
print(max(list3))


#  min()  finds the smallest value from the list
print(min(list3))


'''
LIST COMPREHENSION - List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
'''

list = [1, "ANKAN", "MAITY", 18, 2003]
new_list = []

for items in list:
    new_list.append(items)
print(f"NEW LIST: {new_list}")


# SPLITTING AND JOINING

str = "A.N.K.A.N.M.A.I.T.Y"
list = str.split(".")
s2 = ".".join(list)
print(list)
print(s2)









