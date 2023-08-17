# Concatenating two Strings

name = "ANKAN"
greeting = "Good Morning, "
print(name)
print(type(name))
print(greeting)
print(type(greeting))
c = greeting + name #Concatenating 2 strings
print(c)
print(type(c))

# '''
# The counting of any string starts with 0,1,2,3,4,5,......
# eg:ANKAN -->A=0;N=1;K=2;A=3;N=4
# '''

X = "ANKAN"
print(X[0])

# '''
# String Slicing
# Basic Rule: name=ANKAN & suppose you want to slice "ANK" then u have to write 0:3
# 0:3 ---> only counts from 0 to 2 i.e; 0,1 & 2
# '''

w = "PYTHON"
print(w[0:4])


'''
Slicing with Skip Value
Suppose x= "AnkanIsGood"
then u write print(x[0:5]) the it will show --> Ankan
but if u want to print every 2nd variable then u need to write print(x[0:5:2]) then it will show --> Akn
     "  "  "   "   "     "    3rd   "      "   "   "  "   "    print(x[0:5:3])  "    "  "     "   -->  Aa     
'''

name = "ANKANLOVESCODING"
print(name[0:10:3])
