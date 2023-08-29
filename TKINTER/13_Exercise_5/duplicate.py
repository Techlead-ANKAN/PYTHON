'''Task: - Create GUI form for a dance class where the form will be filled by the students and the name of the students who have filled the forms will be saved in a file.'''

from tkinter import *
from PIL import Image, ImageTk



root = Tk()

'''GUI Logic(s)'''

root.geometry("1920x1080")


# 1st Space label
s0_lb = Label(root, text = "                                                                                                                                                                                                      ")
s0_lb.grid(row = 0, column = 0)

# HEADER
header_lb = Label(root, text = "SUCHI's DANCE CLASSES", font = "arial 14 bold", bg = "black", fg = "white", relief = SUNKEN, bd = 10)
header_lb.grid(row = 0, column = 1, sticky = "NE")

# 2nd Space b/w header and Nataraja Pic
s1_lb = Label(root, text = "                                                                                                                                                      ")
s1_lb.grid(row = 0, column = 2)


# NATARAJA PICTURE
f1 = Frame(root)
f1.grid(row = 0, column = 3, sticky = "W")

nataraja_pic = Image.open("C:\\Users\\mrank\\OneDrive\\Documents\\###  MY WORKS  ###\\[ BACKEND DEVELOPMENT ]\\[ PYTHON ]\\TKINTER\\13_Exercise_5\\NATARAJA_LOGO.png")
resized_nataraja_pic = nataraja_pic.resize((170, 170), Image.ANTIALIAS)
new_nataraja_pic = ImageTk.PhotoImage(resized_nataraja_pic)
nataraja_lb = Label(f1,image = new_nataraja_pic, bd = 1, relief = SUNKEN)
nataraja_lb.grid()

s3_lb = Label(root, text = "                                                                                                                                                                                                                                                                                                                                                                                                                                       d  ")
s3_lb.grid(row = 1, column = 0, columnspan = 3)

# # STUDENT DETAILS FRAME
# f2 = Frame(root, relief = SUNKEN, bd = 1)
# f2.grid(row = 2, column = 0, columnspan = 3)

# # STUDENT DETAILS LABEL
# c_lb = Label(f2, text = "Details of candidate", font = "arial 18 bold")
# c_lb.pack(side = TOP, fill = "x")           

# # CANDIDATE NAME LABEL
# c_name = Label(f2,text = " Name - ", fg = "black", font = "arial 12")
# c_name.grid(row = 1, column = 0)

# # CANDIDATE NAME ENTRY
# c_name_val = StringVar()
# c_name_entry = Entry(f2, textvariable = c_name_val, relief = SUNKEN)
# c_name_entry.grid(row = 1, column = 0, columnspan = 2, padx = 80)

# # CANDIDATE AGE LABEL 
# c_dob = Label(f2, text = " D.O.B - ", fg = "black", font = "arial 12")
# c_dob.grid(row = 2, column = 0, sticky = "W")

# # CANDIDATE D.O.B ENTRY
# c_dob_val = StringVar()
# c_dob_entry = Entry(f2, textvariable = c_dob_val, relief = SUNKEN)
# c_dob_entry.grid(row = 2, column = 0, columnspan = 2)


# # CANDIDATE PHONE NUMBER LABEL
# c_mob = Label(f2,text = " Mob No - ", fg = "black", font = "arial 12")
# c_mob.grid(row = 4, column = 0, sticky = "W")

# # CANDIDATE PHONE NUMBER ENTRY
# c_mob_val = StringVar()
# c_mob_entry = Entry(f2, textvariable = c_mob_val, relief = SUNKEN)
# c_mob_entry.grid(row = 4, column = 0, columnspan = 2)

# # CANDIDATE EMAIL ID LABEL
# c_email = Label(f2,text = " Email Id - ", fg = "black", font = "arial 12")
# c_email.grid(row = 5, column = 0, sticky = "W")

# # CANDIDATE EMAIL ID ENTRY
# c_email_val = StringVar()
# c_email_entry = Entry(f2, textvariable = c_email_val, relief = SUNKEN)
# c_email_entry.grid(row = 5, column = 0, columnspan = 2)

# # CANDIDATE EMAIL ID LABEL
# c_email = Label(f2,text = " Email Id - ", fg = "black", font = "arial 12")
# c_email.grid(row = 5, column = 0, sticky = "W")

# # CANDIDATE EMAIL ID ENTRY
# c_email_val = StringVar()
# c_email_entry = Entry(f2, textvariable = c_email_val, relief = SUNKEN)
# c_email_entry.grid(row = 5, column = 0, columnspan = 2)

# # CANDIDATE ADDRESS LABEL
# c_address = Label(f2, text = " Address - ", fg = "black", font = "arial 12")
# c_address.grid(row = 6, column = 0, sticky = "W")

# # CANDIDATE ADDRESS ENTRY
# c_address_val = StringVar()
# c_address_entry = Entry(f2, textvariable = c_address_val, relief = SUNKEN)
# c_address_entry.grid(row = 6, column = 0, columnspan = 2)

# # CANDIDATE PRIOR EXPERIENCE
# c_ex = Label(f2, text = " Prior Experience - ", fg = "black", font = "arial 12")
# c_ex.grid(row = 7, column = 0, sticky = "W")

# # CANDIDATE PRIOR EXPERIENCE ENTRY
# c_ex_entry = StringVar()
# c_ex_entry = Entry(f2, textvariable = c_ex, relief = SUNKEN)
# c_ex_entry.grid(row = 7, column = 0, columnspan = 2, sticky = "E", ipady = 20)

root.mainloop()