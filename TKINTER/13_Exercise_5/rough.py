'''Task: - Create GUI form for a dance class where the form will be filled by the students and the name of the students who have filled the forms will be saved in a file.'''

from tkinter import *
from PIL import Image, ImageTk



root = Tk()

'''GUI Logic(s)'''

root.geometry("1920x1080")


f1 = Frame(root)
f1.pack(fill = "x")


lb1 = Label(f1, text = "SUCHI'S DANCE CLASSES", bg = "black", fg = "white", font = "arial 18 bold")
lb1.pack(side = TOP, anchor = "center")


nataraja_pic = Image.open("C:\\Users\\mrank\\OneDrive\\Documents\\###  MY WORKS  ###\\[ BACKEND DEVELOPMENT ]\\[ PYTHON ]\\TKINTER\\13_Exercise_5\\NATARAJA_LOGO.png")
resized_nataraja_pic = nataraja_pic.resize((170, 170), Image.ANTIALIAS)
new_nataraja_pic = ImageTk.PhotoImage(resized_nataraja_pic)
lb2 = Label(f1,image = new_nataraja_pic)
lb2.pack(side = RIGHT, anchor = "ne", padx = 20)


f2 = Frame(root, bg = "grey")
f2.pack(fill = "x")

lb3 = Label(f2, text = "Candidate Details", font = "arial 18")
lb3.pack()

f3 = Frame(root, bg = "red", height = 200, width = 200)
f3.pack_propagate(0)
f3.pack(side = LEFT, anchor = "n")

# name = Label(f2, text = "Name - ", fg = "black", font = "arial 14")
# name.grid(row = 0, column = 0)

root.mainloop()