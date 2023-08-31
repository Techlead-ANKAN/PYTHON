# from tkinter import *
# from PIL import Image, ImageTk

# root = Tk()

# root.geometry("1920x1080+0+0")
# root.title("Newspaper")

# # gap2 = Label(root, text = "                                   ")
# # gap2.grid(row = 0, column = 0)

# header_label = Label(text = "Welcome to News Today", bg = "black",fg = "white", font = "arial 20 bold", relief = SUNKEN)
# header_label.grid(row = 0, column = 1, sticky = "W", padx = 170)

# date_label = Label(text = "25.08.2023", font = "robota 10")
# date_label.grid(row = 1, column = 1, sticky = "W", padx = 300)

# # News 1
# pic1 = PhotoImage(file = "C:\\Users\\mrank\\OneDrive\\Documents\\###  MY WORKS  ###\\[ BACKEND DEVELOPMENT ]\\[ PYTHON ]\\TKINTER\\7_Exercise_3\\1.png")
# lb_pic1 = Label(image = pic1, relief = GROOVE, borderwidth=10)
# lb_pic1.grid(row = 2, column = 0)

# lb_text1 = Label(text = '''Chandrayaan-3 LIVE Updates: ISRO on Monday said a two-way communication between the Chandrayaan-2 orbiter and Chandrayaan-3's lander module has been established.
# Chandrayaan-3 was launched from the Satish Dhawan Space Centre in Sriharikota on July 14. (Twitter/Isro)
# Chandrayaan-3 was launched from the Satish Dhawan Space Centre in Sriharikota on July 14. (Twitter/Isro)
# "‘Welcome, buddy!’ Ch-2 orbiter formally welcomed Ch-3 LM. Two-way communication between the two is established. MOX has now more routes to reach the LM," the space agency said in a post on X (formerly Twitter).
# On Sunday,  ISRO announced that the lander module of Chandrayaan-3, the third lunar mission of India, is expected to touch down on the surface of the Moon around 6.04 pm on August 23.
# The live telecast of the landing event will begin at 5.20 pm on Wednesday (August 23).
# "The soft landing of Chandrayaan-3 is a monumental moment that not only fuels curiosity but also sparks a passion for exploration within the minds of our youth," the ISRO said on X (formally Twitter).''', font = "arial 12", justify = LEFT, wraplength = 1000)
# lb_text1.grid(row = 2, column = 1)


# # Gap b/w the 2 news pics
# gap1 = Label(root, text = " ")
# gap1.grid(row = 3, column = 0)

# # News 2
# pic2 = Image.open("C:\\Users\\mrank\\OneDrive\\Documents\\###  MY WORKS  ###\\[ BACKEND DEVELOPMENT ]\\[ PYTHON ]\\TKINTER\\7_Exercise_3\\2.png")
# resized_pic2 = pic2.resize((400, 250), Image.ANTIALIAS)
# new_pic2 = ImageTk.PhotoImage(resized_pic2) 
# lb_pic2 = Label(image = new_pic2, relief = GROOVE, borderwidth = 10)
# lb_pic2.grid(row = 4, column = 0)

# lb_text2 = Label(text = '''Chandrayaan-3 LIVE Updates: ISRO on Monday said a two-way communication between the Chandrayaan-2 orbiter and Chandrayaan-3's lander module has been established.
# Chandrayaan-3 was launched from the Satish Dhawan Space Centre in Sriharikota on July 14. (Twitter/Isro)
# Chandrayaan-3 was launched from the Satish Dhawan Space Centre in Sriharikota on July 14. (Twitter/Isro)
# "‘Welcome, buddy!’ Ch-2 orbiter formally welcomed Ch-3 LM. Two-way communication between the two is established. MOX has now more routes to reach the LM," the space agency said in a post on X (formerly Twitter).
# On Sunday,  ISRO announced that the lander module of Chandrayaan-3, the third lunar mission of India, is expected to touch down on the surface of the Moon around 6.04 pm on August 23.
# The live telecast of the landing event will begin at 5.20 pm on Wednesday (August 23).
# "The soft landing of Chandrayaan-3 is a monumental moment that not only fuels curiosity but also sparks a passion for exploration within the minds of our youth," the ISRO said on X (formally Twitter).''', font = "arial 12", justify = LEFT, wraplength = 1000)
# lb_text2.grid(row = 4, column = 1)


# root.mainloop()



# from tkinter import *

# root = Tk()

# root.geometry("1920x1080")

# f1 = Frame(root)
# f1.pack()

# l1 = Label (f1, text = "Ankan Maity", bg = "cyan")
# l1.grid(row = 0, column = 0)

# l1 = Label (f1, text = "Ankan Maity", bg = "red")
# l1.grid(row = 0, column = 1)

# l1 = Label (f1, text = "Ankan Maity", bg = "blue")
# l1.grid(row = 0, column = 2)

# l1 = Label (f1, text = "Ankan Maity", bg = "green")
# l1.grid(row = 0, column = 3)

# root.mainloop()

# Python3 code to calculate age in years


from datetime import date

def calculateAge(birthDate):
	today = date.today()
	age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
	return age
	
calculateAge(date(1997, 2, 3))

