# Check Button Widget  

# --  It is a standard Tkinter widget that is used to implement ON/OFF selection.
# Check buttons can contain images and texts. when the button is pressed, Tkinter calls that fuction or method.

# Attributes of Check Button: -

# 1) activebackground -- This option used to represent the background color when the checkbutton is under the cursor.
# 2) activeforeground -- This option used to represent the foreground color when the checkbutton is under the cursor.
# 3) bg -- It represents the background colour
# 4) bitmap -- This option used to display a monochrome image on a button.
# 5) bd -- It represents the borderwidth in pixels
# 6) command -- It is used to call a function when the state of the checkbutton is changed
# 7) cursor -- It represents the type of cursor when it is over the checkbutton
# 8) disabledforeground -- The foreground color used to render the text of a disabled checkbutton. The default is a stippled version of the default foreground color.
# 9) font -- It represents the fonts
# 10) fg -- it represents the text colour
# 11) height -- This option used to represent the number of lines of text on the checkbutton and it’s default value is 1.
# 12) highlightcolor: This option used to represent the color of the focus highlight when the checkbutton has the focus.
# 13) image -- It is used to display a graphic image on the button
# 14) justify -- This option used to control how the text is justified: CENTER, LEFT, or RIGHT.
# 15) offvalue -- The associated control variable is set to 0 by default if the button is unchecked. We can change the state of an unchecked variable to some other one.
# 16) onvalue -- The associated control variable is set to 1 by default if the button is checked. We can change the state of the checked variable to some other one. 
# 17) padx -- This option used to represent how much space to leave to the left and right of the checkbutton and text. It’s default value is 1 pixel.
# 18) pady -- This option used to represent how much space to leave above and below the checkbutton and text. It’s default value is 1 pixel.
# 19) relief -- The type of the border of the checkbutton. It’s default value is set to FLAT.
# 20) selectcolor -- This option used to represent the color of the checkbutton when it is set. The Default is selectcolor=”red”.
# 21) selectimage -- The image is shown on the checkbutton when it is set.
# 22) state -- It represents the state of the checkbutton. By default, it is set to normal. We can change it to DISABLED to make the checkbutton unresponsive. The state of the checkbutton is ACTIVE when it is under focus.
# 23) text -- This option used use newlines (“\n”) to display multiple lines of text.
# 24) underline -- This option used to represent the index of the character in the text which is to be underlined. The indexing starts with zero in the text.
# 25) variable -- This option used to represents the associated variable that tracks the state of the checkbutton.
# 26) width -- This option used to represents the width of the checkbutton. and also represented in the number of characters that are represented in the form of texts.
# 27) wraplength -- This option will be broken text into the number of pieces.


# Methods of the Check Button widget: -
# 1) deselect(): This method is called to turn off the checkbutton.
# 2) flash(): The checkbutton is flashed between the active and normal colors.
# 3) invoke(): This method will invoke the method associated with the checkbutton.
# 4) select(): This method is called to turn on the checkbutton.
# 5) toggle(): This method is used to toggle between the different Checkbuttons.


from tkinter import *

root = Tk()
root.geometry("400x400")


check_button = IntVar() # creating a variable that will take only integers (0 or 1) 

button = Checkbutton(root, text = "Want to code!", variable = check_button, offvalue = 0, onvalue = 1)  # creating a checkbutton widget

button.pack()  # packing the check button widget


def get_val():
    if check_button.get() == 0:
        print("Unchecked")
    elif check_button.get() == 1:
        print("Checked")

b1 = Button(root, text = "Click me", command = get_val)
b1.pack()

root.mainloop()