# DICTIONARY METHODS

dictionary = {
        "name": "ANKAN",    
        "fav_numbers": [7, 55, 2],
        "age": 19,
        "anotherdict":  {'title': 'Maity'},
        99 : 89

    
}
# dictionary.keys()--> will print all the keys in a list form
print(dictionary.keys())

# dictionary.items()--> will print all the keys and there coresponding values
print(dictionary.items())

# dictionary.values()--> will print all the values 
print(dictionary.values())

# dictionary.update()--> updates the dictionary by adding pairs of keys and values
updateddict = {
    "dob": "2003"
}

dictionary.update(updateddict)
print(dictionary)




