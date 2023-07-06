'''
DICTIONARY = {keys:values}
'''

# CREATE DICTIONARY
dict = {"NAME":"ANKAN MAITY","AGE":18,"D.O.B": 2003, 1:2}
print(dict)


# EMPTY DICTIONARY
dict = {}
print(f"This is how u create an empty dictionary: {dict}")


# ACCESS ELEMENTS FROM DICTIONARY

dict = {
    "key1":"value1",
    1:2
}
print(dict[1])    #--->  This will print the "value" corresponding the given "key"  


dict = {"NAME":"ANKAN MAITY","AGE":18,"D.O.B": 2003, 1:2}
print(dict['NAME'])  
print(dict["AGE"])
print(dict[1])
print(dict["D.O.B"])

# SAMPLE DICT
dict = {"NAME":"ANKAN MAITY","AGE":18,"D.O.B": 2003, 1:2,3:4}
dict2 = {99:88}

# Method	                Description

# 1.clear()	               Removes all the elements from the dictionary
dict.clear()
print(dict)


# 2.copy()	               Returns a copy of the dictionary
clone = dict.copy()
print(f"This is a copy of the original dict: {clone}")


# 3.fromkeys()	           Returns a dictionary with the specified keys and value
a = (1,3,5)
b = (2,4)
res = dict.fromkeys(a,b)
print(res)


# 4.get()	               Returns the value of the specified key
print(dict.get("NAME"))


# 5.items()	                Returns a list containing a tuple for each key value pair
print(dict.items())


# 6.keys()	                Returns a list containing the dictionary's keys
print(dict.keys())


# 7.pop()	                Removes the element with the specified key
a = dict.pop("AGE")
print(a)
print(f"This is the dict afer poping an element: {dict}")


# 8.popitem()	            Removes the last inserted key-value pair
b = dict.popitem()
print(b)


# 9.setdefault()	        Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
a = dict.setdefault(1)
print(a)


# 10.update()	            Updates the dictionary with the specified key-value pairs
dict.update(dict2)
print(dict)


# 11.values()	            Returns a list of all the values in the dictionary
print(dict.values())
