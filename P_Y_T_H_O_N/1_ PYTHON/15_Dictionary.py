'''
DICTIONARY
SYNTAX
"key":"values can be both string and number or a List of numbers"
'''

dictionary = {
        "name": "ANKAN",    
        "fav_numbers": [7, 55, 2],
        "age": 19,
        "anotherdict":  {'title': 'Maity'},
        99 : 89

    
}

print(dictionary["name"])  # Will print ANKAN
print(dictionary['fav_numbers'])  # Will print [7, 55, 2]
print(dictionary['age'])   # Will print 19
print(dictionary['anotherdict']['title'])   # Will print Maity
print(dictionary[99])  # Will print 89



seconddictionary = {
    "marks": [1, 2, 3, 4, 5]
}


# changing the values (VALUES IN A DICTIONARY CAN BE CHANGED)

seconddictionary['marks'] = [9,8,7]

print(seconddictionary['marks'])
