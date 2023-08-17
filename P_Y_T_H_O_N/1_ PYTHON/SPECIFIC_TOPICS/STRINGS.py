'''
STRING - METHODS
'''

str = "This is the string that i am going to use for most of the methods"
s = "ankanisagoodboy"
L = len(str)
str1 = "APPLE"
str3 = "Ankan"
L1 = len(str1)
tuple = ("only", "myself", "ankan")
str2 = "25.58"


# 1) string.capitalize()  -> Capitalizes the first character of the string.
print("#1")
res = s.capitalize()
print(res)


# 2) string.center(width,fillchar) -->  Returns a space padded string centered to a total of width columns.
a = str1.center(20)
print("#2")
print(a)


# 3) string.counter(string,start,end)  --> counts how many times the required string is present in a string.
print("#3")
print(str.count("string",0,L))


# 4) decode(encoding='UTF-8',errors='strict')  --> Decodes the string using the code registered for encoding.


# 5) encode(encoding='UTF-8',errors= 'strict') --> Returns encoded version of the string: on error, default is to raise a value error unless error is given with 'ignore' or 'replace'


# 6) string.endswith(str,start,end) --> Determines if the string ends with specifed string or not. True if it ends with the req. string or False.
print("#6")
print(str.endswith("methods"))


# 7) expandtabs(tab_size)  -> Normally size of tab is 4 white spaces. Now you can change the size of the tab.
_str = "\tA\tN\tK\tA\tN\t"
print("#7")
print(_str.expandtabs(99))


# 8) string.find(str,start,end) --> Finds the req. str in the string.
print("#8")
print(str.find("methods"))


# 9) string.index(str,start,end) --> Finds the index or position of the str.
print("#9")
print(str.index("t"))


# 10) string.isalnum() --> Returns True if string has atleast 1 character and all characters are alphanumeric.
print("#10")
print(str.isalnum())


# 11) string.isalpha() --> Returns True if string has atleast 1 character and all charcaters are alphabetic and False otherwise.
print("#11")
res1 = s.isalpha()
print(res1)


# 12) string.isdigit() --> Returns true if string contains only digit and False otherwise.
print("#12")
print(str.isdigit())


# 13) string.islower() --> Returns True if atleast 1 character is lower case and all cased characters
print("#13")
print(str.islower())


# 14) string.isnumeric() --> Returns True if a string contains only numeric characters.
print("#14")
print(str.isnumeric())


# 15) string.isspace() --> Returns True if the string contains only white space charaters.
print("#15")
print(str.isspace())


# 16) string.istitle() --> Returns True if the string is perfectly title-cased(first letter is CAPS and the rest is SMALL).
print("#16")
print(str3.istitle())


# 17) string.isupper() --> Returns True  if the string has all upper-case alphabets.
print("#17")
print(str1.isupper())


# 18) string.join(iterable) --> The join() method takes all items in an iterable and joins them into one string. 
# A string must be specified as the separator.
x = "#".join(tuple)
print("#18")
print(x)


# 19) len(string) --> finds the length of the string
print("#19")
print(len(str))


# 20) string.ljust(width,[fillchar]) --> Returns a space paded string with the original string left justified to a total of width columns
print("#20")
print(str1.ljust(20), "HI")


# 21) string.lower() --> Converts all the characters of a string into a lower case characters
print("#21")
print(str1.lower())


# 22) string.lstrip() --> Removes all leading white spaces
print("#22")
print(str.lstrip())


# 23) string.maketrans() --> Returns a translation table to be used in translate function
final = str1.maketrans("A","S")
print("#23")
print(str1.translate(final))


# 24) max(string) --> Returns the highest alphabetical character(character with highest ASCII value) from the string
print("#24")
print(max(str))


# 25) min(string) --> Returns the lowest alphabetical charcater(charceter with lowest ASCII value) from the string.
print("#25")
print(min(str1))


# 26) string.replace(old,new) --> Replace a character .
print("#26")
print(str.replace("this","ANKAN"))


# 27) string.rfind(str,start,end) --> Reverse find
print("#27")
print(str.rfind("the"))


# 28) string.rindex(str,start,end)  --> Reverse index
print("#28")
print(str.rindex("i"))


# 29)  string.rjust(width,[fillchar]) --> Returns a space padeed string with the original string right justified to a total of width columns
print("#29")
print(str.rjust(20))


# 30) string.rstrip --> Remoces all trailing white spaces
print("#30")
print(str.rstrip())


# 31) string.split(str="",num= string.count(str)) --> 
print("#31")
print(str.split("method",str.count("method")))


# 32) string.splitlines(num = string.count('\n'))  -> split string at new lines
print("#32")
print(str.count('\n'))


# 33) string.startswith(str,start,end) --> 
print("#33")
print(str.startswith("this"))


# 34) strip([chars])



# 35) string.swapcase() --> inverts all character's cases
print("#35")
print(str.swapcase())


# 36) string.title() --> returns perfectly titled 
print("#36")
print(str.title())


# 37)trasnalate(table, deletechars ="")


# 38) string.upper() --> converts lower case to upper case
print("#38")
print(str.upper())


# 39) string.zfil()
print("#39")
print(str1.zfill(15))


# 40) string.isdecimal() --> 
print("#40")
print(str2.isdecimal())

    
