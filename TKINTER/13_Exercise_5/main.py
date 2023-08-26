'''Task: - Create GUI form for a dance class where the form will be filled by the students and the name of the students who have filled the forms will be saved in a file.'''

from tkinter import *
from PIL import Image, ImageTk

root = Tk()

'''GUI Logic(s)'''

root.geometry("1920x1080")

# HEADER
header_lb = Label(root, text = "SUCHI's DANCE CLASSES", font = "arial 14 bold")
header_lb.grid(row = 0, column = 0, padx = 550, sticky = "NE")

# NATARAJA PICTURE
nataraja_pic = Image.open("C:\\Users\\mrank\\OneDrive\\Documents\\###  MY WORKS  ###\\[ BACKEND DEVELOPMENT ]\\[ PYTHON ]\\TKINTER\\13_Exercise_5\\NATARAJA_LOGO.png")
resized_nataraja_pic = nataraja_pic.resize((170, 170), Image.ANTIALIAS)
new_nataraja_pic = ImageTk.PhotoImage(resized_nataraja_pic)
nataraja_lb = Label(image = new_nataraja_pic)
nataraja_lb.grid(row = 0, column = 1, sticky = "N")

# CANDIDATE NAME LABEL
c_name = Label(text = "Candidate Name - ", fg = "black", font = "arial 14")
c_name.grid(row = 1, column = 0, sticky = "NW")

# CANDIDATE NAME ENTRY
c_name_val = StringVar()
c_name_entry = Entry(root, textvariable = c_name_val, relief = SUNKEN)
c_name_entry.grid(row = 1, column = 0, sticky = "W", padx= 165)

# CANDIDATE AGE LABEL 
c_age = Label(text = "Candidate Age - ", fg = "black", font = "arial 14")
c_age.grid(row = 2, column = 0, sticky = "W")

# # CANDIDATE AGE ENTRY
c_age_val = IntVar()
c_age_entry = Entry(root, textvariable = c_age_val, relief = SUNKEN)
c_name_entry.grid(row = 2, column = 0, sticky = "W", padx = 165)

root.mainloop()