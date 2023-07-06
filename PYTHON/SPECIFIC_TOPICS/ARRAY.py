'''
ARRAY
'''

# Creating array
import array as arr

a = arr.array("i",[1,2,3,4,5])
for i in a:
    print(i)

# INTEGER TYPE 
import array as arr

a = arr.array("i",[1,2,3,4,5])
for i in a:
    print(i)

# FLOAT TYPE
import array as arr

a = arr.array("f",[1.0,2.587,3.478951,4.01,599.12])
for i in a:
    print(i)

# DOUBLE TYPE
import array as arr

a = arr.array("d",[1.0,2.587,3.478951,4.01,599.12])
for i in a:
    print(i)

# Access elements 
# array_name(index)
 
# METHODS
import array as arr
b = arr.array("i", [1,2,3,4,5,6])

# 1)Addition
b.insert(2,4.98)
b.append(4089)
print(b)

# 2) Remove
b.pop(2)  #-> removes element at position 2
b.remove(1)  # -> removes the first ccurrence of 1

# 3) Slicing
b[0:3]

# 4) index
b.index(3)  # -> index of first occurrence of the element


# 5) Upadting elements
b[3] = 99


