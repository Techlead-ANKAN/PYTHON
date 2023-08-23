# Frames in Tkinter

# A frame in Tkinter is used to organize the group of widgets. It acts like a container which can be used to hold the othre widgets. The rectangular areas of the screen are used to organize the widgets to the python application. 

# Syntax: -
# <variable> = Frame(master, options,.....)

#  Attributes of Frame: -
# 1) bd -- It represents the border width
# 2) bg -- It represents the background colour of the widget
# 3) cursor -- It determines the type of cursor will be shown while hovering over the frame
# 4) height -- It represents the vertical dimension of the new frame
# 5) highlightcolor -- It is used to represent the colour of the fous highlight when the frame has the focus
# 6) highlightthickness -- This option used to represent the thickness of the focus highlight.
# 7) highlightbackground -- This option used to represent the color of the focus highlight when the frame does not have focus. 
# 8) relief -- The type of the border of the frame. It’s default value is set to FLAT.
# 9) width -- This option used to represents the width of the frame.


from tkinter import *

root = Tk()
root.geometry("1920x1080")

''' GUI Logic(s)'''

f1 = Frame(root, bg = "cyan", height = 400, width = 400, borderwidth = 2, relief = RIDGE)   # Creating the frame

f1.pack(side = TOP)    # Packing the frame

f1.pack_propagate(0)   # By default the frame fits its content, but this statement packs the frame according to the dimension given, 
                       # without considering its content

root.mainloop()