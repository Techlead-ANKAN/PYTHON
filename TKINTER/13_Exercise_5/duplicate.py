'''Task: - Create GUI form for a dance class where the form will be filled by the students and the name of the students who have filled the forms will be saved in a file.'''

from tkinter import *
from PIL import Image, ImageTk



root = Tk()

'''GUI Logic(s)'''

root.geometry("1920x1080")

# FIRST FRAME
f1 = Frame(root)
f1.pack(fill = "x")

# DANCE LOGO (LEFT SIDE)
logo = Image.open("C:\\Users\\mrank\\OneDrive\\Documents\\###  MY WORKS  ###\\[ BACKEND DEVELOPMENT ]\\[ PYTHON ]\\TKINTER\\13_Exercise_5\\dance_logo.png")
resized_logo = logo.resize((170, 170), Image.ANTIALIAS)
pic = ImageTk.PhotoImage(resized_logo)
lb3 = Label(f1, image = pic)
lb3.grid(row = 0, column = 0)

# SPACE B\W LOGO AND HEADER
sp_logo_header = Label(f1, text = "                                                                                                                     ")
sp_logo_header.grid(row = 0, column = 1)

# HEADER LABEL
header_lb = Label(f1, text = "SUCHI'S DANCE CLASSES", bg = "maroon",relief = GROOVE, bd = 7, fg = "white", font = "arial 18 bold", padx = 8, pady = 4)
header_lb.grid(row = 0, column = 2, sticky  = "n")

# ADDRESS AND DETAILS OF INSTITUTE LABEL(s)
details__lb = Label(f1, text = "14/1, Verner Lane, Belgharia\nKolkata - 700056, West Bengal, India\nPhone - 8617790081, Email - mr.ankanmaity@gmail.com", font = "arial 14", justify = "center")
details__lb.grid(row = 0, column = 2)

# SPACE B\W HEADER AND NATARAJA PIC
sp_header_nat = Label(f1, text = "                                                                                                               ")
sp_header_nat.grid(row = 0, column = 3)

# NATARAJA PIC (RIGHT SIDE)
nataraja_pic = Image.open("C:\\Users\\mrank\\OneDrive\\Documents\\###  MY WORKS  ###\\[ BACKEND DEVELOPMENT ]\\[ PYTHON ]\\TKINTER\\13_Exercise_5\\NATARAJA_LOGO.png")
resized_nataraja_pic = nataraja_pic.resize((170, 170), Image.ANTIALIAS)
new_nataraja_pic = ImageTk.PhotoImage(resized_nataraja_pic)
nataraja_lb = Label(f1,image = new_nataraja_pic)
nataraja_lb.grid(row = 0, column = 4, sticky = "ne")

# SECOND FRAME
f2 = Frame(root)
f2.pack(fill = "x", side = TOP)

# CANDIDATE DETAILS LABEL
lb3 = Label(f2, text = "Candidate Details", font = "arial 18", bg = "black", fg = "white", relief = SUNKEN, bd = 8)
lb3.pack()

# GAP B/W 2ND FRAME AND 3RD FRAME
gap = Label(f2, text = " ")
gap.pack()


# THIRD FRAME
f3 = Frame(root, height = 200, width = 200)
# f3.pack_propagate(0)
f3.pack(fill = "x", side = TOP)


# NAME LABEL
name = Label(f3, text = "Name - ", fg = "black", font = "arial 14")
name.grid(row = 0, column = 0)

# NAME ENTRY
name_val = StringVar()
name_entry = Entry(f3, textvariable = name_val)
name_entry.grid(row = 0, column = 1, ipadx = 20, ipady = 2)

# SPACE B/W NAME AND GUARDIAN
s1 = Label(f3, text = "            ")
s1.grid(row = 0, column = 2)

# GUARDIAN LABEL
guardian = Label(f3, text = "Guardian - ", fg = "black", font = "arial 14")
guardian.grid(row = 0, column = 3)

# GUARDIAN ENTRY
guardian_val = StringVar()
guardian_entry = Entry(f3, textvariable = guardian_val)
guardian_entry.grid(row = 0, column = 4, ipadx = 20, ipady = 2)

# SPACE B/W GUARDIAN AND AGE
s2 = Label(f3, text = "            ")
s2.grid(row = 0, column = 5)

# AGE LABEL
age = Label(f3, text = "Age - ", fg = "black", font = "arial 14")
age.grid(row = 0, column = 6)

# AGE ENTRY
age_val = IntVar()
age_entry = Entry(f3, textvariable = age_val)
age_entry.grid(row = 0, column = 7, ipadx = 20, ipady = 2)

# SPACE B/W AGE AND MOB
s3 = Label(f3, text = "            ")
s3.grid(row = 0, column = 8)

# MOBILE LABEL
mob = Label(f3, text = "Mobile - ", fg = "black", font = "arial 14")
mob.grid(row = 0, column = 9)

# MOBILE LABEL
mob_val = StringVar()
mob_entry = Entry(f3, textvariable = mob_val)
mob_entry.grid(row = 0, column = 10, ipadx = 20, ipady = 2)

# SPACE B/W MOBILE AND LOCATION
s4 = Label(f3, text = "            ")
s4.grid(row = 0, column = 11)

# LOCATION LABEL
loc = Label(f3, text = "Address - ", fg = "black", font = "arial 14")
loc.grid(row = 0, column = 12)

# LOCATION ENTRY
loc_val = StringVar()
loc_entry = Entry(f3, textvariable = loc_val)
loc_entry.grid(row = 0, column = 13, ipadx = 88, ipady = 2)

# GAP BETWEEN ROW-0 AND ROW-1
gap1 = Label(f3, text = "")
gap1.grid(row = 1, column = 0)

# EMAIL-ID LABEL
email = Label(f3, text = "Email Id - ", fg = "black", font = "arial 14")
email.grid(row = 2, column = 0)

# EMAIL-ID ENTRY
email_val = StringVar()
email_entry = Entry(f3, textvariable = email_val)
email_entry.grid(row = 2, column = 1, ipadx = 20, ipady = 2)

# SPACE B/W EMAIL-ID AND PRIOR EXPERIENCE
s5 = Label(f3, text = "            ")
s5.grid(row = 2, column = 2)

# PRIOR EXPERIENCE LABEL
prior_ex = Label(f3, text = "Prior Experience - ", fg = "black", font = "arial 14")
prior_ex.grid(row = 2, column = 3)

# PRIOR EXPERIENCE ENTRY
prior_ex_val = StringVar()
prior_ex_entry = Entry(f3, textvariable = prior_ex_val)
prior_ex_entry.grid(row = 2, column = 4, ipadx = 42, ipady = 2)

# SPACE B/W PRIOR EXPERIENCE AND EXPERIENCE TIME
s6 = Label(f3, text = "            ")
s6.grid(row = 2, column = 5)

# EXPERINCE LABEL
ex_time = Label(f3, text = "Experience(in months/years) - ", fg = "black", font = "arial 14")
ex_time.grid(row = 2, column = 6)

# EXPERIENCE ENTRY
ex_time_val = StringVar()
ex_time_entry = Entry(f3, textvariable = ex_time_val)
ex_time_entry.grid(row = 2, column = 7, ipadx = 20, ipady = 2)

# SPACE B\W EXPERIENCE TIME AND DOMAIN
s7 = Label(f3, text = "            ")
s7.grid(row = 2, column = 8)

# DOMAIN LABEL
domain = Label(f3, text = "Interested Domain - ", fg = "black", font = "arial 14")
domain.grid(row = 2, column = 9)

# DOMAIN ENTRY
domain_val = StringVar()
domain_entry = Entry(f3, textvariable = domain_val)
domain_entry.grid(row = 2, column = 10, ipadx = 20, ipady = 2)


# FOURTH FRAME
f4 = Frame(root)
f4.pack(side = TOP, pady = 30, fill = "x")

# COURSE DETAILS LABEL
c_details = Label(f4, text = "Course Details", font = "arial 18",  bg = "black", fg = "white", relief = SUNKEN, bd = 8)
c_details.pack(side = TOP, anchor = "n")

# FIFTH FRAME
f5 = Frame(root)
f5.pack(side = TOP, fill = "x")

# COURSE TYPE LABEL


def get_candidate_details():

    print("-------Candidate Details-------\n")
    print(f"Candidate Name - {name_val.get()}\n")
    print(f"Guardian - {guardian_val.get()}\n")
    print(f"Age - {age_val.get()}\n")
    print(f"Mobile No. - {mob_val.get()}\n")
    print(f"Address - {loc_val.get()}\n")
    print(f"Email Id - {email_val.get()}\n")
    print(f"About Prior Experience - {prior_ex_val.get()}\n")
    print(f"Experience Period - {ex_time_val.get()}\n")
    print(f"Interested Domain - {domain_val.get()}\n")



root.mainloop()