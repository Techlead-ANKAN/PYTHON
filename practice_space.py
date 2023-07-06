# Topics to practice: -
# 1) String 
# 2) List 
# 3) Tuple 
# 4) Sets 
# 5) Dictionaries 
# 6) Loops
# 7) Functions
# 8) Recursions
# 9) File


'''STRINGS PROBLEMS'''

# Basic String Programs
# 1) Python program to check whether the string is Symmetrical or Palindrome
s1 = "121"

if s1[0:len(s1)] == s1[len(s1)::-1]:
    print("Palindrome / Symmetrical")
else:
    print("Not Palindrome / Symmetrical")


# 2) Reverse words in a given String in Python
s2 = "I am doing Python"

x = s2.split()[::-1]

print(" ".join(x))


# 3) Ways to remove i’th character from string in Python
s3 = "Ankan Maity"
new = ""
L = len(s3)
i = int(input("Enter the index: "))

for j in range(len(s3)):
    if j != i:
        new += s3[j]

print(new)


# 4) Find length of a string in python (4 ways)

s4 = "Ankan is a good boy."

#   way - 1 (len function)
l = len(s4)
print(l)

#   way - 2 (for loop)
i = 0
for char in str:
    i += 1
print(i)

#   way - 3 (while loop)
j = 0
while s4[j:]:
    j += 1
print(j)

#   way - 4 (function)
def find_len(a):
    k = 0
    for ele in a:
        k += 1
    return (k)

print(find_len(s4))


# 5) Python – Avoid Spaces in string length
s5 = "Ankan is doing python."
r5 = 0
for char in s5:
    if char != " ":
        r5 += 1
print(r5)


# 6) Python program to print even length words in a string
s6 = "Hi how are You, it is a sunny day"
list = s6.split()[::1]
print(list)
r6 = []
for words in list:
    if words.isalpha():
        if len(words) % 2 == 0:
            r6.append(words)
    
print(r6)


# 7) Python – Uppercase Half String
s7 = "abcdef"
length = len(s7)
r7 = ""

for i in range(int(length/2)):
    r7 += s7[i].lower()

for j in range(int(length/2),length):
    r7 += s7[j].upper()

print(r7)

# 8) Python program to capitalize the first and last character of each word in a string

s8 = "Ankan is a good boy."
L = len(s8)
w = s8.split()[::1]
new = []
final = []
rev = s8.split()[::-1]


for words in w:
    new.append(words.capitalize())

for words in new:
    

print(new)





# Python program to check if a string has at least one letter and one number
# Python | Program to accept the strings which contains all vowels
# Python | Count the Number of matching characters in a pair of string
# Python program to count number of vowels using sets in given string
# Python Program to remove all duplicates from a given string
# Python – Least Frequent Character in String
# Python | Maximum frequency character in String
# Python – Odd Frequency Characters
# Python – Specific Characters Frequency in String List
# Python | Frequency of numbers in String
# Python | Program to check if a string contains any special character
# Generating random strings until a given string is generated
# Find words which are greater than given length k
# Python program for removing i-th character from a string
# Python program to split and join a string
# Python | Check if a given string is binary string or not
# Python | Find all close matches of input string from a list
# Python program to find uncommon words from two Strings
# Python | Swap commas and dots in a String
# Python | Permutation of a given string using inbuilt function
# Python | Check for URL in a String
# Execute a String of Code in Python

# Advance String Programs
# Python | Convert numeric words to numbers
# Python | Word location in String
# Python | Consecutive characters frequency
# String slicing in Python to rotate a string
# String slicing in Python to check if a string can become empty by recursive deletion
# Python Program to find minimum number of rotations to obtain actual string
# Python – Words Frequency in String Shorthands
# Python – Successive Characters Frequency
# Python – Sort String list by K character frequency
# Python – Convert Snake case to Pascal case
# Python – Avoid Last occurrence of delimitter
# Python program to find the character position of Kth word from a list of strings
# Python – Right and Left Shift characters in String
# Python | Exceptional Split in String
# Python – Split String on vowels
# Python – Mirror Image of String
# Python – Replace multiple words with K
# Python – Replace Different characters in String at Once
# Python | Multiple indices Replace in String
# Python – Ways to remove multiple empty spaces from string List
# Python | Remove punctuation from string
# Python – Similar characters Strings comparison
# Python – Remove K length Duplicates from String
# Python – Remove suffix from string list
# Python Counter| Find all duplicate characters in string
# Python – Replace duplicate Occurrence in String
# Ways to convert string to dictionary
# Python – Check if two strings are Rotationally Equivalent
# Python | Test if string is subset of another
# Python Program to Generate Random binary string
# Python Program to convert binary to string
# Python – Reverse Sort a String

# Programs on SubString
# Python | Check if a Substring is Present in a Given String
# Python – Substring presence in Strings List
# Python – All substrings Frequency in String
# Python – Maximum Consecutive Substring Occurrence
# Python – Maximum occurring Substring from list
# Python – Possible Substring count from String
# Python – Replace all occurrences of a substring in a string
# Python – Longest Substring Length of K
# Python – Extract Indices of substring matches
# Python | Split by repeating substring
# Python | Remove substring list from String
# Python – Remove after substring in String
# Python | Remove Reduntant Substrings from Strings List
# Python – Test substring order
# Python – String till Substring
# Python – Filter Strings combination of K substrings