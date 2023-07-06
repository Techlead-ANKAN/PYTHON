'''
PRACTICE SET - 5
'''

# 1) write a program to create dictionary of hindi words with values as their english translations

dict = {
    "seb" : "apple",
    "chappal" : "sandal",
    "bistar"  :  "bed",
    "bharosa" : "trust"
}

print("Options are: ",(dict.keys()))
a = input("Enter a hindi word: ")
print("The translation of the Hindi word in English is ", dict[a])

# 2)  write a program to input 8 numbers by the user and print all the unique numbers.
a = int(input("Enter 1st num. "))
b = int(input("Enter 2nd num  ")) 
c = int(input("Enter 3rd num  "))
d = int(input("Enter 4th num  "))
e = int(input("Enter 5th num  "))
f = int(input("Enter 6th num  "))
g = int(input("Enter 7th num  "))
h = int(input("Enter 8th num  "))

s ={ a, b, c, d, e, f, g, h}
print(s)

# 3) can we have 18(int) and "18"(string) in a set
b ={18, "18"}
print(b) # yes 

# 4) 
s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(s)


# 5) what is type of s in : s = {}
s = {}
print(type(s)) # DICTIONARY


# 6)
x = {}
a = input("Enter your favourite language Shreya: ")
b = input("Enter your favourite language Ankan: ")
c = input("Enter tour favourite language Jeet:  ")
d = input("Enter your favourite language Somali: ")


x['Shreya'] = a
x['Ankan'] = b
x['Jeet'] = c
x['Somali'] = d

print(x)

# 7)
x = {}
a = input("Enter your favourite language Shreya: ")
b = input("Enter your favourite language Ankan: ")
c = input("Enter tour favourite language Jeet:  ")
d = input("Enter your favourite language Jeet: ")


x['Shreya'] = a
x['Ankan'] = b
x['Jeet'] = c
x['Jeet'] = d # WIll always print the latest value whic is entered at the last

print(x)

# 8)
x = {}
a = input("Enter your favourite language Shreya: ")
b = input("Enter your favourite language Ankan: ")
c = input("Enter tour favourite language Jeet:  ")
d = input("Enter your favourite language Somali: ")


x['Shreya'] = a
x['Ankan'] = b
x['Jeet'] = c
x['Somali'] = d 

print(x)

# 9)
s = {8, 7, 12, "Harry", [1,2]}
# --> you cannot change the  item in the list present in the set 's'. 
