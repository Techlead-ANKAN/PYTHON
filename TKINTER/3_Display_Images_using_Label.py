from tkinter import *

root = Tk()

''' GUI Logic(s)'''

root.geometry("700x500")  # setting the dimension of the GUI

pic = PhotoImage(file = "C:\\Users\\mrank\\OneDrive\\Documents\\###  MY WORKS  ###\\[ BACKEND DEVELOPMENT ]\\[ PYTHON ]\\TKINTER\\Model1.png")

lb = Label(image = pic)
lb.pack()

root.mainloop()