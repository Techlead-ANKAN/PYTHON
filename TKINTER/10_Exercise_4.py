'''
Task - Create 4 buttons stacked horizontaly, where each button should print some text after clicking.
'''

from tkinter import *

root = Tk()

root.geometry("600x500+500+200")
root.title("Exercise - 4")

frame = Frame(root, bg = "grey", relief = SUNKEN, height = 80, width = 285)
frame.pack_propagate(0)
frame.pack(side = TOP, anchor = "n", pady = 200)

def f1():
    print("I am a Red button.")

def f2():
    print("I am a Blue button.")

def f3():
    print("I am a Green button.")

def f4():
    print("I am an Orange button.")

b1 = Button(frame, text = "Click Me", fg = "red", bg = "white", activebackground = "red", activeforeground = "white", height = 3,  width = 7, command = f1)
b1.pack(side = LEFT, padx = 10, pady = 10)

b2 = Button(frame, text = "Click Me", fg = "blue", bg = "white", activebackground = "blue", activeforeground = "white", height = 3,  width = 7, command = f2)
b2.pack(side = LEFT, pady = 10)

b3 = Button(frame, text = "Click Me", fg = "green", bg = "white", activebackground = "green", activeforeground = "white", height = 3,  width = 7, command = f3)
b3.pack(side = LEFT, padx = 10, pady = 10)

b4 = Button(frame, text = "Click Me", fg = "orange", bg = "white", activebackground = "orange", activeforeground = "white", height = 3,  width = 7, command = f4)
b4.pack(side = LEFT, pady = 10)

root.mainloop()
