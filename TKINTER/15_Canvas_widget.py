# Canvas 

# -- The Canvas is a rectangular area intended for drawing pictures or other complex layouts. You can place graphics, text, widgets or frames on a Canvas.

# Syntax: -
# <variable> = Canas(master, options, .....)

# Attributes of Canvas: -
# 1) bd -- It represents the borderwidth in pixels. (Default = 2)
# 2) bg -- It represents the normal background colour
# 3) confine -- If True(the default), the canvas cannot be scrollled outside the scroll-region.
# 4) cursor -- Used in the circle like arrow, circle, dot, etc.
# 5) height -- Size of the canvas in y-dimension
# 6) highlightcolor -- Color shown in the focus highlight
# 7) relief -- It specifies the type of border.
# 8) scrollregion -- A tuple(w, n, e, s) that defines over how large an area the canvas can be scrolled, where w is the left side, n is the top side, e is the right side and s is the bottom side
# 9) width -- size of the canvas in x-direction
# 10) xscrollincrement -- If you set this option to some positive dimension, the canvas can be positioned only on multiples of that distance, and the value will be used for scrolling by scrolling units, such as when the user clicks on the arrows at the ends of a scrollbar.
# 11) xscrollcommand -- If the canvas is scrollable, this attribute should be the .set() method of the horizontal scrollbar.
# 12) yscrollincrement -- Works like xscrollincrement, but governs vertical movement.
# 13) yscrollcommand -- If the canvas is scrollable, this attribute should be the .set() method of the vertical scrollbar.


from tkinter import *

root = Tk()

canvas_width = 500
canvas_height = 500

root.geometry(f"{canvas_width}x{canvas_height}")   # geometry of the GUI


c1 = Canvas(root, width = canvas_width, height = canvas_height, bg = "cyan")  # Creating a canvas
c1.pack()   # packing the canvas


# Item	            Method

# Line	         create_line()
# Rectangle	    create_rectangle()
# Oval	         create_oval()
# Arc	          create_arc()
# Polygon	      create_polygon()
# Text	         create_text()
# Image	         create_image()

# 1) Creating a line
# Syntax: - <canvas_variable>.create_line((X1, Y1), (X2, Y2), options...)
c1.create_line((0,0), (500, 500), fill = "blue")

# 2) Creating a rectangle
# Syntax: - <canvas_variable>.create_rectangle((TOP_LEFT co-ordinates), (BOTTOM_RIGHT co-ordintates), options...)
c1.create_rectangle((150, 150), (300, 300))

# 3) Creating a text
# Syntax: - <canvas_variable>.create_text((starting co-ordinates), options...)
c1.create_text((100, 200), text = "Ankan Maity")

# 4) Creating an oval
# Syntax: - <canvas_variable>.create_oval((TOP_LEFT co-ordinates of the rectngle in which ovel will be drawn), (BOTTOM_RIGHT co-ordintates  of the rectngle in which oval will be drawn), options...)
c1.create_oval((100, 100), (400, 200))

# 5) Creating a polygon
# Syntax: - <canvas_variable>.create_polygon((X1,Y1), (X2, Y2), (X3, Y3), (Xn, Yn), options...)
c1.create_polygon((50,50), (100,100), (0,100))

# 6) Creating a image
# Syntax: - <canvas_variable>.create_image((X,Y), options...)
pic = PhotoImage(file = "C:\\Users\\mrank\\OneDrive\\Documents\\###  MY WORKS  ###\\[ BACKEND DEVELOPMENT ]\\[ PYTHON ]\\TKINTER\\13_Exercise_5\\dance_logo.png")
c1.create_image((150, 50), image = pic)

# 7) Creating an arc
# Syntax: - <canvas_variable>.create_arc((X1,Y1), (X2,Y2), options...)
c1.create_arc((100, 100), (200, 200), style = PIESLICE)  # Creating a PIESLICE
c1.create_arc((100, 100), (200, 200), style = CHORD)     # Creating a CHORD
c1.create_arc((100, 100), (200, 200), style = ARC)       # Creating an ARC

root.mainloop()