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

print(new)








# 9) Python program to check if a string has at least one letter and one number

s9 = "Ankan's age is 20."
letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
flag = 0
for char in s9:
    if char in letters or numbers:
        flag = 1
    else:
        flag = 0


if flag == 1:
    print("Atleast one number and alphabet present")
else:
    print("Atleast one number and alphabet is not present")


# 10) Python | Program to accept the strings which contains all vowels

s10 = input("Enter a string: ")
vowels = "aeiou"
flag = 0
for char in s10:
    if char in vowels:
        flag = 1
    else:
        flag = 0

if flag == 1:
    print("String accepted")
else:
    print("String not accepted")


# 11) Python | Count the Number of matching characters in a pair of string

s11 = "aabbcdef"
s_11 = "axybbz"
dup = []
res11 = []
for char in s11:
    if char in s_11:
        if char not in dup:
            dup.append(char)
            res11.append(char)

print(f"No.of Matching characters:{len(res11)}")


# 12) Python program to count number of vowels using sets in given string
s12 = "Ankan is a good boy"
vowels = "aeiou"
final12 = set()

for char in s12:
    if char in vowels:
        final12.add(char)

print(len(final12))

# 13) Python Program to remove all duplicates from a given string
s13 = "Ankan is a good boy"
res13 = ""

for char in s13:
    if char not in res13:
        res13 += char

print(res13)



# 14) Python – Least Frequent Character in String
s14 = "Geeks for geeks"
unq14 = ""
no = []
ch = []
for char in s14.lower():
    if char not in unq14:
        unq14 += char
        no.append((s14.lower()).count(char))
        ch.append(char)

print(ch)
print(no)

i = no.index(min(no))

print(f"Maximum Frequency character: {ch[i]} and Frequency is: {no[i]}")





# 15) Python | Maximum frequency character in String
s15 = "Geeks for geeks"
unq15 = ""
no = []
ch = []
for char in s15.lower():
    if char not in unq15:
        unq15 += char
        no.append((s15.lower()).count(char))
        ch.append(char)

print(ch)
print(no)

i = no.index(max(no))

print(f"Maximum Frequency character: {ch[i]} and Frequency is: {no[i]}")
        


# 16) Python – Odd Frequency Characters
s15 = "Geeks for geeks"
unq15 = ""
no = []
ch = []
res15 =""
for char in s15.lower():
    if char not in unq15:
        unq15 += char
        no.append((s15.lower()).count(char))
        ch.append(char)

print(ch)
print(no)

for i in range(len(no)):
    if no[i]!=0:
        if no[i]%2!=0:
            res15 += ch[i]

print(res15)



# 16) Python – Specific Characters Frequency in String List
s16 = "geeksforgeeks is the best"
l16 = ['g', 'i', 'b', 'e']

for char in l16:
    if char in s16:
        print(f"{char} --> {s16.count(char)}")
        s16.replace(char,"")

    


# 17) Python | Frequency of numbers in String
s17 = "geeks4feeks is No. 1 4 geeks"
counter = 0

for char in s17:
    if char.isnumeric():
        counter += 1
print(f"No. of numbers in the string are: {counter}")


# 18) Python | Program to check if a string contains any special character
s18 = "Geeks$ForGeeks"
flag = 0
for char in s18:
    if not (char.isalpha() or (char.isdigit()) or (char == " ")):
        flag = 1
    else:
        flag = 0
    
if flag == 1:
    print("String not accepted")
else:
    print("String accepted")

# 19) Generating random strings until a given string is generated



# 20) Find words which are greater than given length k
s20 = "Ankan is a good boy"
k = 3
l20 = s20.split()[::1]

for words in l20:
    if len(words) > k:
        print(words)


# 21) Python program for removing i-th character from a string
s21 = "Ankan is a good boy"
k = int(input("enter index: "))
for i in range(len(s21)):
    if i == k:
        res21 = s21.replace(s21[i], "")
        break

print(res21)


# 22) Python program to split and join a string
s22 = "Ankan is a good boy"
l22 = s22.split()[::1]
print(f"After splitting: {l22}")
j22 = " ".join(l22)
print(f"After joining: {j22}")

# 23) python | Check if a given string is binary string or not
s23 = "101010101"
flag = 0
for char in s23:
    if (char==0) or (char==1):
        flag = 1
    else:
        flag = 0

if flag == 1:
    print("Binary String")
else:
    print("Not a Binary String")


# 24) Python | Find all close matches of input string from a list
from difflib import get_close_matches
patterns = ['ape', 'apple', 'peach', 'puppy']
word = 'apple'
print(get_close_matches(word, patterns))


 # 25) Python program to find uncommon words from two Strings
s25 = "Geeks for Geeks"
s_25 = "Learning from Geeks for Geeks"

l25 = set(s25.split()[::1])
l_25 = set(s_25.split()[::1])


res25 = set()

if len(l25) > len(l_25):
    res25 = (l25.difference(l_25))
elif len(l_25) > len(l25):
    res25 = (l_25.difference(l25))

for ele in res25:
    print(ele)



# 26) Python | Swap commas and dots in a String
s26 = "14, 625, 498.002"

res26 = s26.replace(',','@')
res26 = res26.replace('.',',')
res26 = res26.replace('@','.')
print(res26)


# 27) Python | Permutation of a given string using inbuilt function
from itertools import permutations

s27 = "ABC"
perm_list = list(permutations(s27))
print(type(perm_list))

for perms in perm_list:
    print("".join(perms))

# 28) Python | Check for URL in a String
# 29) Execute a String of Code in Python
code = '6+5'
res29 = eval(code)
print(res29) 


# Advance String Programs

# 30) Python | Convert numeric words to numbers
dict = {"one": 1, "two": 2, "three" : 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0}

s30 = "zero four zero one"
l30 = s30.split()[::1]
res30 = ""

for ele in l30:
    res30 = res30 + str(dict.get(ele))
   

print(res30)


# 31) Python | Word location(not index) in String
s31 = "geeksforgeeks is best for geeks"
word = "best"
l31 = s31.split()[::1]

for ele in l31:
    if ele == word:
        print(l31.index(word)+1)


# 32) Python | Consecutive characters frequency
s32 = "geekksforgggeeks"
count = 1
no = []
char = []
res32 = {}
for i in range(0,(len(s32)-1)):
    if (s32[i] == s32[i+1]):
        count += 1
    else:
        char.append(s32[i])
        no.append(count)
        count = 1

print(no)
print(char)  # Main program complete


for i in range(0, len(char)-1):
    print(f" {char[i]} --> {no[i]}")




# 33) String slicing in Python to rotate a string
s33 = "GeeksforGeeks"
n = 2

print(f"Left rotation: {s33[2:] + s33[0:2]}") 
print(f"Right rotation: {s33[-2:] + s33[0:-2]}")

# 34) String slicing in Python to check if a string can become empty by recursive deletion
s34 = "GeeksforGeeks"
s34 = s34.lower()
word = "geeks"

if s34.find(word):
    s34.replace(word, "")

print(s34)

# 35) Python Program to find minimum number of rotations to obtain actual string

# 36) Python – Words Frequency in String Shorthands

s36 = "Gfg is is best"
l36 = s36.split()[::1]
dup36 = []
unq36 = []

counter = 0
for words in l36:
    if words not in dup36:
        dup36.append(words)
        unq36.append(words)


for words in unq36:
    print(f"{words} --> {l36.count(words)}")


# 37) Python – Successive Characters Frequency
s37 = "geeks are for geeksforgeeks"
word37 = "geek"
wrd_len = len(word37)
count = 0
a = s37.index(word37)
letter = a + wrd_len

for i in range(letter, len(s37)):
    if s37[i] == "s":
        count += 1

print(count)


# 38) Python – Sort String list by K character frequency
s38 = ["geekforgeekss", "is", "bessst", "for", "geeks"]
k = 's'
no = []
final = []
for words in s38:
    count = 0
    if k in words:
        for i in range(len(words)):
            if words[i] == k:
                count += 1
        no.append(count)
    else:
        no.append(0)


largest = max(no)

for i in range(0,len(no)-1):
    if no[i] == largest:
        a = no.pop(i)
        # print(largest)
        print(no)
        print(s38[i])
    largest = max(no)
    

print(no)




# 39) Python – Convert Snake case to Pascal case
s39 = "I_am_a_good_boy" #S nake case
l39 = s39.split('_')[::1]
res39 = []
print(l39)

for word in l39:
    res39.append(word.capitalize())

Pascal_case = " ".join(res39)

print(Pascal_case)


# 40) Python – Avoid Last occurrence of delimitter
l40 = [4, 7, 8, 3, 2, 1, 9]
res40 = []
for i in l40:
    res40.append(str(i))

    
delim = "*"
s40 = delim.join(res40)
print(s40)


# 41) Python program to find the character position of Kth word from a list of strings
l41 = ["geekforgeeks", "is", "best", "for", "geeks"]
k = 21
s41 = ""
for i in l41:
    s41 += i
char = s41[k]

print(s41.find(char))



# 42) Python – Right and Left Shift characters in String

# 43) Python | Exceptional Split in String
s43 = "gfg, is, (best, for), geeks"
l43 = []
temp43 = ""
for char in s43:
    if char == '(':
        if char != ')':
            temp43 += char
        elif char == ')':
            l43.append(temp43)
            temp43 = ""

    elif char != '(':
        if char != ',':
            temp43 += char
        elif char == ',':
            l43.append(temp43)
            temp43 = ""        

print(l43)




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