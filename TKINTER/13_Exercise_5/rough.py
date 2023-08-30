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


logo = Image.open("C:\\Users\\mrank\\OneDrive\\Documents\\###  MY WORKS  ###\\[ BACKEND DEVELOPMENT ]\\[ PYTHON ]\\TKINTER\\13_Exercise_5\\dance_logo.png")
resized_logo = logo.resize((170, 170), Image.ANTIALIAS)
pic = ImageTk.PhotoImage(resized_logo)
lb3 = Label(f1, image = pic)
lb3.pack(side = TOP, anchor = "nw", padx = 20)

f2 = Frame(root)
f2.pack(fill = "x")

lb3 = Label(f2, text = "Candidate Details", font = "arial 18", bg = "black", fg = "white", relief = SUNKEN, bd = 8)
lb3.pack()

gap = Label(f2, text = " ")
gap.pack()

f3 = Frame(root, height = 200, width = 200)
# f3.pack_propagate(0)
f3.pack(fill = "x")

name = Label(f3, text = "Name - ", fg = "black", font = "arial 14")
name.grid(row = 0, column = 0)

name_val = StringVar()
name_entry = Entry(f3, textvariable = name_val)
name_entry.grid(row = 0, column = 1, ipadx = 20, ipady = 2)

s1 = Label(f3, text = "            ")
s1.grid(row = 0, column = 2)

guardian = Label(f3, text = "Guardian - ", fg = "black", font = "arial 14")
guardian.grid(row = 0, column = 3)

guardian_val = StringVar()
guardian_entry = Entry(f3, textvariable = guardian_val)
guardian_entry.grid(row = 0, column = 4, ipadx = 20, ipady = 2)

s2 = Label(f3, text = "            ")
s2.grid(row = 0, column = 5)

age = Label(f3, text = "Age - ", fg = "black", font = "arial 14")
age.grid(row = 0, column = 6)

age_val = IntVar()
age_entry = Entry(f3, textvariable = age_val)
age_entry.grid(row = 0, column = 7, ipadx = 20, ipady = 2)

s3 = Label(f3, text = "            ")
s3.grid(row = 0, column = 8)

mob = Label(f3, text = "Mobile - ", fg = "black", font = "arial 14")
mob.grid(row = 0, column = 9)

mob_val = StringVar()
mob_entry = Entry(f3, textvariable = mob_val)
mob_entry.grid(row = 0, column = 10, ipadx = 20, ipady = 2)

s4 = Label(f3, text = "            ")
s4.grid(row = 0, column = 11)

loc = Label(f3, text = "Address - ", fg = "black", font = "arial 14")
loc.grid(row = 0, column = 12)

loc_val = StringVar()
loc_entry = Entry(f3, textvariable = loc_val)
loc_entry.grid(row = 0, column = 13, ipadx = 88, ipady = 2)

gap1 = Label(f3, text = "")
gap1.grid(row = 1, column = 0)

email = Label(f3, text = "Email Id - ", fg = "black", font = "arial 14")
email.grid(row = 2, column = 0)

email_val = StringVar()
email_entry = Entry(f3, textvariable = email_val)
email_entry.grid(row = 2, column = 1, ipadx = 20, ipady = 2)

s5 = Label(f3, text = "            ")
s5.grid(row = 2, column = 2)

prior_ex = Label(f3, text = "Prior Experience - ", fg = "black", font = "arial 14")
prior_ex.grid(row = 2, column = 3)

prior_ex_val = StringVar()
prior_ex_entry = Entry(f3, textvariable = prior_ex_val)
prior_ex_entry.grid(row = 2, column = 4, ipadx = 42, ipady = 2)

s6 = Label(f3, text = "            ")
s6.grid(row = 2, column = 5)

ex_time = Label(f3, text = "Experience(in months/years) - ", fg = "black", font = "arial 14")
ex_time.grid(row = 2, column = 6)

ex_time_val = IntVar()
ex_time_entry = Entry(f3, textvariable = ex_time_val)
ex_time_entry.grid(row = 2, column = 7, ipadx = 20, ipady = 2)

s7 = Label(f3, text = "            ")
s7.grid(row = 2, column = 8)

domain = Label(f3, text = "Interested Domain - ", fg = "black", font = "arial 14")
domain.grid(row = 2, column = 9)

domain_val = StringVar()
domain_entry = Entry(f3, textvariable = domain_val)
domain_entry.grid(row = 2, column = 10, ipadx = 20, ipady = 2)

root.mainloop()