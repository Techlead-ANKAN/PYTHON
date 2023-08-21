'''
Task - Create a GUI of dimension 500 x 400 with a  narrow strip(label) at the bottom of the GUI, that will show "READY"
'''


from tkinter import *

root = Tk()
root.title("Ankan's GUI")

root.geometry("500x400")
lb = Label(text = "READY!!!", bg = "black", fg = "white", font = "arial 22 bold", relief = RAISED)
lb.pack(side = BOTTOM, anchor = "s", fill = X)

root.mainloop()