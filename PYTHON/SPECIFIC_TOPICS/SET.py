'''
SET - It is an unordered collection of unique elements.
'''

# CREATE A SET:
# set = {1,2,True, "Ankan",25.98}
# print(f"This is how u create a set: {set}")


# EMPTY SET:
# set = {}
# print(f"This is how u create an empty test: {set}")


# CHANGE IN SET:
 
# 1) ADDING ELEMENT  
# set = {1,2,True, "Ankan",25.98}

# set.add(99)
# set.add("hi")
# set.add(False)

# print(set)

# 2) ADDING LIST, TUPLE, SET IN A SET

# set = {1,2,True, "Ankan",25.98}

# Adding set to a set
# set.update({"set",18})
# print(set)

# Adding List to a set
# set.update(["list",33])
# print(set)

# Adding Tuple to a set
# set.add(("abcd"))
# print(set)

# Adding list and tuple simultaneously to a set
# set.update({"set"}, ["list"])
# print(set)


# 3) REMOVING ELEMENTS FROM THE SET

# Using remove(1 arguement)
# set.remove(2)
# set.remove(1)

# print(set)

# using discard(1 arguement)
# set.discard(2)
# set.discard("Ankan")

# print(set)



'''
Set Methods
'''
set1 = {1,2,True, "Ankan",25.98}
set2 = {1,2,3}
set3 = {3,4,5}
set4 = {9,8,7}
set5 = {"a","b", 3,4,5}
set6 = {"apple","banana","lemon"}
set7 = {"microsoft","google","apple"}

# Method	                                           Description

# 1. add()	                                        Adds an element to the set
# set1.add("add")
# print(set1)


# 2.clear()	                                    Removes all the elements from the set
# set1.clear()
# print(set1)


# 3.copy()	                                    Returns a copy of the set
# print(f"Clone of original set: {set1.copy()}")


# 4.difference()	                                Returns a set containing the difference between two or more sets
# diff1 = set2.difference(set3)
# diff2 = set3.difference(set2)
# print(diff1)
# print(diff2)

# 5.difference_update()	                        Removes the items in this set that are also included in another, specified set
# set2.difference_update(set3)
# print(set2)
# set3.difference_update(set2)
# print(set3)


# 6.discard()	                                    Remove the specified item
# set1.discard(2)
# print(set1)


# 7.intersection()	                            Returns a set, that is the intersection of two or more sets
# intersection = set1.intersection(set2)
# print(intersection)


# 8.intersection_update()	                        Removes the items in this set that are not present in other, specified set(s)
# set2.intersection_update(set3)
# print(set2)


# 9.isdisjoint()	                                Returns whether two sets are totally different or not
# a = set2.isdisjoint(set4)
# print(a)


# 10.issubset()	                                Returns whether another set contains this set or not
# b = set3.issubset(set5)
# print(b)

# 11.issuperset()	                                Returns whether this set contains another set or not
# z = set5.issuperset(set3)
# print(z)


# 12.pop()	                                        Removes an element from the set
# y = set2.pop(2)
# print(y)

# 13.remove()	                                    Removes the specified element
# set1.remove(1)
# print(set1)


# 14.symmetric_difference()	                    Returns a set with the symmetric differences of two sets
# ass = set2.symmetric_difference(set3)
# print(ass)


# 15.symmetric_difference_update()	                inserts the symmetric differences from this set and another
# set6.symmetric_difference_update(set7)
# print(set6)

# 16.union()	                                    Return a set containing the union of sets
# union = set2.union(set3)
# print(union)


# 17.update()	                                    Update the set with another set, or any other iterable
# set1.update({"shreya"})
# print(set1)