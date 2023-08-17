# Counting Vowels

str = input("Enter any string: ")
vowels = ('a', 'e', 'i', 'o', 'u')
count = 0
for char in str:
    if char.lower() in vowels:
        count += 1

print(f"No.of Vowels in the string are: {count}")