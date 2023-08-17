'''
List Methods (only mostly used are here: list.append() is the mostly used method)
'''

l1 = [55, 25, 4, 100, 15]

# list.sort() --> updates the list in INCREASING order
l1.sort()
print(l1)

# list.reverse() --> reverses the list
l1.reverse()
print(l1)

# list.append() --> adds a value at the end of the list. Eg: list.append(5)- then it will add 5 at the end of the list
l1.append(21)
print(l1)

# list.insert() --> inserts a value at your desired position or index. Syntax-list.insert(position/index where you want to insert a value,the value you want to insert)
l1.insert(3, 180)
print(l1)

# list.pop() --> removes the value from that index/position.Synatx-list.pop(position/index of the value you want to remove)
l1.pop(2)
print(l1)

# list.remove() --> the item you want to remove from the list
l1.remove(25)
print(l1)


