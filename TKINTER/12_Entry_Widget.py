# Entry Widget -- The Entry Widget is a Tkinter Widget used to Enter or display a single line of text. 

# Attributes of Entry widget: -
# 1) bg -- represents the normal background colour
# 2) bd -- The size of the border around the indicator. Default is 2 pixels
# 3) font -- The font used for text
# 4) fg -- represents the foreground colour
# 5) justify -- if the text contains multiple lines, this option controls how the lines will be aligned
# 6) relief -- border style
# 7) show -- Normally, the characters that the user types appear in the entry. To make a .password. entry that echoes each character as an asterisk, set show=”*”.
# 8) textvariable -- In order to be able to retrieve the current text from your entry widget, you must set this option to an instance of the StringVar class.

# Syntax: -
# <variable> = Entry(master, options,...)

from tkinter import *

def get_vals():
    print(f"User - {userval.get()}")
    print(f"Password - {passval.get()}")

root = Tk()
root.geometry("300x300")


# There are a total of 4 variable class in Tkinter: -  
# BooleanVar - Holds Boolean, returns 0 for False and 1 for True
# StringVar - Holds a string, default value = ""
# IntVar - Holds an integer, default value = 0
# DoubleVar - Holds a float, default value = 0.0


user_label = Label(text = "User", font = "arial 10 bold")
user_label.grid(row = 0, column = 0, sticky = "E")

pass_label = Label(text = "Password", font = "arial 10 bold")
pass_label.grid(row = 1, column = 0, sticky = "E")

userval = StringVar()
passval = StringVar()

userentry = Entry(root, textvariable = userval)
userentry.grid(row = 0, column = 1,)

passentry = Entry(root, textvariable = passval, show = "!")
passentry.grid(row = 1, column = 1)

sub_button = Button(root, text = "Submit", bg = "cyan", fg = "black", height = 1, width = 9, relief = RIDGE, command = get_vals)
sub_button.grid(row = 2, column = 1, sticky = "w")

root.mainloop()

