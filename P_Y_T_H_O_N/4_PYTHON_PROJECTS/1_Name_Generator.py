# Name Generator 

# using "names" module to generate names according to gender

import names

name_list = []
n = int(input("Enter no.of names to be generated: "))
sex = input("Enter gender: ")

if sex.lower() == "male" or sex.lower() == "m":
    for i in range(0, n):
        name_list.append(names.get_full_name(gender="male"))

elif sex.lower() == "female" or sex.lower() == "f":
    for i in range(0, n):
        name_list.append(names.get_full_name(gender="female"))

else:
    for i in range(0, n):
        name_list.append(names.get_full_name())

print("Generated Names: ")
for name in name_list:
    print(f"* {name}")
