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

# YES OR NO CHECK BUTTON
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

# GAP BETWEEN ROW-1 AND ROW-2
gap2 = Label(f3, text = "")
gap2.grid(row = 3, column = 0)

# LOCATION LABEL
loc = Label(f3, text = "Address - ", fg = "black", font = "arial 14")
loc.grid(row = 4, column = 0)

# LOCATION ENTRY
loc_val = StringVar()
loc_entry = Entry(f3, textvariable = loc_val)
loc_entry.grid(row = 4, column = 1, columnspan = 4, ipadx = 88, ipady = 2, sticky = "W")


# FOURTH FRAME
f4 = Frame(root)
f4.pack(side = TOP, pady = 30, fill = "x")

# COURSE DETAILS LABEL
c_details = Label(f4, text = "Course Details", font = "arial 18",  bg = "black", fg = "white", relief = SUNKEN, bd = 8)
c_details.pack(side = TOP, anchor = "n")

# FIFTH FRAME
f5 = Frame(root)
f5.pack(side = TOP, fill = "x")

# DANCE TYPE LABEL
d_form = Label(f5, text = "   ⚫ Select Dance style - (Write 'Yes' to the dance style you want as a subject)", font = "arial 14")
d_form.grid(row = 0, column = 0)

# GAP B/W DANCE TYPE LABEL AND TYPES
gap2 = Label(f5, text = "")
gap2.grid(row = 1, column = 0)

# 6TH FRAME
f6 = Frame(root)
f6.pack(side = TOP, fill = "x")

s8 = Label(f6, text = "     ")
s8.grid(row = 0, column = 0)

# BHARATNATYAM CHECK BUTTON
d1_val = IntVar()
Checkbutton(f6, text = "Bharatnatyam", variable = d1_val, font = "arial 14", offvalue = 0, onvalue = 1).grid(row = 0, column = 1)

s9 = Label(f6, text = "     ")
s9.grid(row = 0, column = 2)

# KATHAK CHECK BUTTON
d2_val = IntVar()
Checkbutton(f6, text = "Kathak", variable = d2_val, font = "arial 14", offvalue = 0, onvalue = 1).grid(row = 0, column = 3)

s10 = Label(f6, text = "     ")
s10.grid(row = 0, column = 4)

# ODISSI CHECK BUTTON
d3_val = IntVar()
Checkbutton(f6, text = "Odissi", variable = d3_val, font = "arial 14", offvalue = 0, onvalue = 1).grid(row = 0, column = 5)

s11 = Label(f6, text = "     ")
s11.grid(row = 0, column = 6)

# JHUMAIR CHECK BUTTON
d4_val = IntVar()
Checkbutton(f6, text = "Jhumair", variable = d4_val, font = "arial 14", offvalue = 0, onvalue = 1).grid(row = 0, column = 7)

s12 = Label(f6, text = "     ")
s12.grid(row = 0, column = 8)

# INDIAN CLASSICAL DANCE CHECK BUTTON
d5_val = IntVar()
Checkbutton(f6, text = "Indian Classical", variable = d5_val, font = "arial 14", offvalue = 0, onvalue = 1).grid(row = 0, column = 9)

s13 = Label(f6, text = "     ")
s13.grid(row = 0, column = 10)

# GARBA CHECK BUTTON
d6_val = IntVar()
Checkbutton(f6, text = "Garba", variable = d6_val, font = "arial 14", offvalue = 0, onvalue = 1).grid(row = 0, column = 11)

s14 = Label(f6, text = "     ")
s14.grid(row = 0, column = 12)

# MOHININATYAM CHECK BUTTON
d7_val = IntVar()
Checkbutton(f6, text = "Mohininatyam", variable = d7_val, font = "arial 14", offvalue = 0, onvalue = 1).grid(row = 0, column = 13)

# GAP B/W DANCE TYPE LABEL AND TYPES
gap3 = Label(f6, text = "")
gap3.grid(row = 2, column = 0)

f7 = Frame(root)
f7.pack(side = TOP, fill = "x")

# BATCHES LABEL
batch_lb = Label(f7, text = "   ⚫ Select Batch - ", font = "arial 14")
batch_lb.grid(row = 0, column = 0)

# BATCHES
batches = ["Monday [4:30p.m.]", "Tuesday [4:30p.m.]", "Wednesday [4:30p.m.]", "Thursday [4:30p.m.]", "Friday [4:30p.m.]", "Saturday [4:30p.m.]", "Sunday [4:30p.m.]"]

value_inside = StringVar(root)
value_inside.set("Select a Batch")

s15 = Label(f7, text = "   ")
s15.grid(row = 0, column = 1)

menu = OptionMenu(f7, value_inside, *batches)
menu.grid(row = 0, column = 2)

# GAP B/W BATCHES AND FEES
gap4 = Label(f7, text = "")
gap4.grid(row = 1, column = 0)

f8 = Frame(root)
f8.pack(side = TOP, fill = "x")

# COURSES LABEL
course_lb = Label(f8, text = "   ⚫ Select Course - ", font = "arial 14")
course_lb.grid(row = 0, column = 0)

# COURSES
courses = ["Bharatnatyam - 1500/-", "Kathak - 1200/-", "Odissi - 1250/-", "Jhumair - 1300/-", "Indian Classical - 1600/-", "Garba - 900/-", "Mohininatyam - 1100/-"]

value_inside = StringVar(root)
value_inside.set("Select Course - ")

s16 = Label(f8, text = "   ")
s16.grid(row = 0, column = 1)

menu = OptionMenu(f8, value_inside, *courses)
menu.grid(row = 0, column = 2)

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