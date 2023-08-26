# Grid in Tkinter
# The master GUI is split into a no.of rows and columns that can hold widgets. The grid geometry manager puts the widget in a 2 dimensional table.

# Syntax: -
# < widget >.grid(master, options)


# Attributes of grid: -

# 1) column -- specifies the column
# 2) columnspan -- It specifies the no.of columns the widget occupies
# 3) ipadx, ipady -- It specifies the no.of pixels to pad the widget, horizontally and vertically inside the widget's borders.
# 4) row -- spcifies the row
# 5) rowspan -- It specifies the no.of rows the widget occupies
# 6) sticky -- If the cell is larger than the widget, then with the help of "sticky"  you can allocate the widget in parts  like --> N, E, S, W, NE, NW, SE, and SW of the cell.



from tkinter import *

root = Tk()
root.geometry("400x400")

user = Label(root, text = "UserId", bg = "blue")   # Creating a widget (label as a sample) to place in a grid
user.grid(row = 0, column = 0)        # packing the widget using the grid() function.

# *** NOTE -- In a program you can use only one either "pack()" or "grid()", using both at the same program will cause error 

password = Label(root, text = "Password", bg = "red")
password.grid(row = 0, column = 1, columnspan = 2)

sample = Label(root, text = "this is along text that will occupy more.", bg = "cyan")
sample.grid(row = 1, column = 0, columnspan = 2)


root.mainloop()



''' grid_location() -- This method is used to rerieve the relative grid location on the parent widget '''

from tkinter import * 

root = Tk()

b=Button(root, text="00")
b.grid(row=0, column=0)

b2=Button(root, text="11")
b2.grid(row=1, column=1)

b3=Button(root, text="22")
b3.grid(row=2, column=2)

b4=Button(root, text="33")
b4.grid(row=3, column=3)

b5=Button(root, text="44")
b5.grid(row=4, column=4)

def mouse(event):
    print(event.x, event.y)
    print(root.grid_location(event.x, event.y))

root.bind("<Button-1>", mouse)   # binding the click method with the mouse

root.mainloop()


'''forget_pack() --  This will remove the widget from toplevel basically widget do not get deleted it just becomes invisible and loses its position and can be retrieve'''

from tkinter import *
from tkinter.ttk import *

# toplevel window
root = Tk()

# method to make widget invisible
# or remove from toplevel
def forget(widget):

	# This will remove the widget from toplevel
	# basically widget do not get deleted
	# it just becomes invisible and loses its position
	# and can be retrieve
	widget.forget()

# method to make widget visible
def retrieve(widget):
	widget.pack(fill = BOTH, expand = True)

# Button widgets
b1 = Button(root, text = "Btn 1")
b1.pack(fill = BOTH, expand = True)

# See, in command forget() method is passed
b2 = Button(root, text = "Btn 2", command = lambda : forget(b1))
b2.pack(fill = BOTH, expand = True)

# In command retrieve() method is passed
b3 = Button(root, text = "Btn 3", command = lambda : retrieve(b1))
b3.pack(fill = BOTH, expand = True)


root.mainloop()
