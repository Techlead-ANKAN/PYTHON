# Buttons in Tkinter

# The button widget is a standard Tkinter widget, which is used for various kinds of buttons. A button is a widget that is designed for the user to interact with that is if the button is pressed by mouse click some action might be started, they can also contain text and images like labels. 

# Syntax: -
# <variable> = Button(master, options)

# 1) activebackground -- it represents the background of the button when the mouse hover the button
# 2) activeforeground -- It represents the font color of the button when the mouse hover the button
# 3) bd -- It represents the borderwidth in pixels
# 4) bg -- It represents the background color of the button
# 5) command -- It will call the function that is being scheduled when the button is being clicked
# 6) fg -- It represents the foreground color of the button
# 7) height -- It represents the height of the button
# 8) highlightcolor -- The color of the highlight when the button has the focus.
# 9) image -- It is used to set the image to be displayed on the button.
# 10) justify -- It illustrates the way multiple text lines are represented.
# 11) padx -- padding in x-direction
# 12) pady -- padding in y-direction
# 13) relief -- type of border
# 14) state - the option is set to DISABLED to make the button unresponsive and ACTIVE to make the button responsive
# 15) underline -- to make the button's text underlined
# 16) wraplength -- The length is set to a positive number, which means that the text lines will be wrapped to fit within this length.


from tkinter import *

root = Tk()

root.geometry("1920x1080")

f1 = Frame(root)
f1.pack()

def greet():
    print("Hello nice to meet you!!!")

b1 = Button(f1, text = "Click Me!!!\nNOW", activebackground = "white", activeforeground = "black", bg = "grey", fg = "white", bd = 3, command = greet, height = 2, width = 9, justify = CENTER, padx = 100, pady = 100, relief = RIDGE, underline = 0)
b1.pack(side = LEFT)


root.mainloop()