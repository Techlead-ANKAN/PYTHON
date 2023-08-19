'''
1) Geometry/Dimension of the GUI  ---> geometry()
2) Minimum size of the GUI  ---> minsize()
3) Maximum size of the GUI ---> maxsize()
4) Creating a Label ---> Label()
5) Packing the label in the GUI ---> pack()
'''


from tkinter import *     # importing all the modules from the Tkinter library

root = Tk()

''' GUI Logic(s)'''

# 1) Geometry / Dimension of GUI   
# syntax: - geometry("width x height")
# About - The geometry("width x height + < horizontal shift (L to R)> + < Vertical shift (U to D)") method is a fundamental method that is used to determine the position, dimension of the layout of the GUI.
root.geometry("400x300")      # --> This will create a the GUI of the given dimensions at any position of the screen
root.geometry("500 x 400 + 200 + 150")  # -- > This will create a the GUI of the given dimensions at the position of the screen as per the last 2 parameter given.


# 2) Setting Minimum size of GUI
# syntax: - minsize(width, height) 
root.minsize(300, 200)

# 3) Setting Maximum size of GUI
# syntax: - maxsize(width, height) 
root.maxsize(800, 700)

# 4) Setting Label (It is a thing that cannot be interacted by the user)
# syntax: - < variable > = Label (text = " <label text> ")
Ankan = Label(text = "This is a label.")

Ankan.pack()   # pack() method packs the label in the gui and shows the Label in the GUI

root.mainloop()