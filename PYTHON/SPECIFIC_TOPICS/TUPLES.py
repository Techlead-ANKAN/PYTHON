'''
TUPLES
'''


# EMPTY TUPLE:
tuple = ()
print(tuple)


# Tuple is IMMUTABLE


# Deleting using : del statement
tuple = (1,2,3,4,5,6)
print(f"Before deleting: {tuple}")
del tuple
print(tuple)


# METHODS
tup1 = (1,2,3,4,5,6)
tup2 = (3,4,5,6,7,8)
list = [1,2,3,4,5,6]


# 1. cmp(tuple1, tuple2) --> Compares elements from both the tuples
# print(cmp(tup1, tup2))


# 2. len(tuple) --> Gives the total length of the tuple
print(len(tup1))


# 3. max(tuple)  --> Returns item from the tuple with maximum value
print(max(tup2))


# 4. min(tuple) --> Returns item from the tuple with minimum value
print(min(tup1))


# 5. tuple(seq) --> Converts a list into tuple
print(tuple(list))


