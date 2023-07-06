'''
Practice Set - 3
'''

# Question-1
# Display a user entered name followed by " Good Afternoon" using input() func.

greeting = " Good Afternoon "
name = input("Enter your name: ")
print( greeting + name)


# Question-2
# Fill in a letter template below with name and date
#  letter = ''' Dear <|NAME|>
# you are selected!
# <|DATE|>'''

letter =  ''' Dear <|NAME|>
you are selected

<|DATE|>
''' 

name = input("Enter your name: ")
date = input("Enter date: ")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)

# Question-3
# Detect Double Spaces in a String

story = "  Ankan  is  a  good  boy.  He  is one of the best programmer out there."
print(story.count("  "))

# Question-4
# Reaplace Double Spaces from problem 3 into Single Spaces

story = "  Ankan  is  a  good  boy.  He  is one of the best programmer out there."
singlespace = " "
story = (story.replace("  ",singlespace))
print(story)

# Question-5
# Format the following letter using Escape Sequence characters

letter = " \\Dear Harry,\nThis Python course is nice.\tThank\'s"
print(letter)

