'''
Task - There are many images (png) in a directory, and the no.of images are given to you and corresponding to that images ther are some news regarding that image. So what we have to do is create a newspaper GUI with it.
'''

from tkinter import *
from PIL import Image, ImageTk


root = Tk()

''' GUI Logic(s) '''

root.geometry("1920x1080+0+0")

# Title of the GUI
root.title("Newspaper")

# Header
header_label = Label(text = "Welcome to News Today", bg = "black",fg = "white", font = "arial 20 bold", relief = SUNKEN)
header_label.pack(side = TOP, anchor = "n")

# Date
date_label = Label(text = "21.08.2023", font = "robota 10")
date_label.pack(side = TOP, anchor = "n")

# 1st Frame
f1 = Frame(root)
f1.pack(side = TOP, anchor = "nw", fill = "x")

# Shift 1st pic
s1 = Label(f1, text = "             ")
s1.grid(row = 0, column = 0)

# News 1
pic1 = Image.open("C:\\Users\\mrank\\OneDrive\\Documents\\###  MY WORKS  ###\\[ BACKEND DEVELOPMENT ]\\[ PYTHON ]\\TKINTER\\7_Exercise_3\\1.png")
resized_pic1 = pic1.resize((350, 200), Image.ANTIALIAS)
new_pic1 = ImageTk.PhotoImage(resized_pic1) 
lb_pic1 = Label(f1, image = new_pic1, relief = GROOVE, borderwidth=10)
lb_pic1.grid(row = 0, column = 1)

# Shift 1st text
s2 = Label(f1, text = "              ")
s2.grid(row = 0, column = 2)

lb_text1 = Label(f1, text = '''Chandrayaan-3 LIVE Updates: ISRO on Monday said a two-way communication between the Chandrayaan-2 orbiter and Chandrayaan-3's lander module has been established.
Chandrayaan-3 was launched from the Satish Dhawan Space Centre in Sriharikota on July 14. (Twitter/Isro)
Chandrayaan-3 was launched from the Satish Dhawan Space Centre in Sriharikota on July 14. (Twitter/Isro)
"‘Welcome, buddy!’ Ch-2 orbiter formally welcomed Ch-3 LM. Two-way communication between the two is established. MOX has now more routes to reach the LM," the space agency said in a post on X (formerly Twitter).
On Sunday,  ISRO announced that the lander module of Chandrayaan-3, the third lunar mission of India, is expected to touch down on the surface of the Moon around 6.04 pm on August 23.
The live telecast of the landing event will begin at 5.20 pm on Wednesday (August 23).
"The soft landing of Chandrayaan-3 is a monumental moment that not only fuels curiosity but also sparks a passion for exploration within the minds of our youth," the ISRO said on X (formally Twitter).''', font = "arial 12", justify = LEFT, wraplength = 1000)
lb_text1.grid(row = 0, column = 3)

# gap b/w f1 and f2
gap1 = Label(f1, text = "")
gap1.grid(row = 1, column = 0)

# 2nd Frame
f2 = Frame(root)
f2.pack(side = TOP, anchor = "nw", fill = "x")

# Shift 2nd pic
s3 = Label(f2, text = "             ")
s3.grid(row = 0, column = 0)

# News 2
pic2 = Image.open("C:\\Users\\mrank\\OneDrive\\Documents\\###  MY WORKS  ###\\[ BACKEND DEVELOPMENT ]\\[ PYTHON ]\\TKINTER\\7_Exercise_3\\2.png")
resized_pic2 = pic2.resize((350, 200), Image.ANTIALIAS)
new_pic2 = ImageTk.PhotoImage(resized_pic2) 
lb_pic2 = Label(f2, image = new_pic2, relief = GROOVE, borderwidth = 10)
lb_pic2.grid(row = 0, column = 1)

# shift 2nd text
s3 = Label(f2, text = "             ")
s3.grid(row = 0, column = 2)

lb_text2 = Label(f2, text = '''September has always been an exciting month for tech, particularly due to the fact that Apple unveils its shiny new iPhones in that time. This year, it’s a bit different though, as some surprises and innovations from other players in the tech industry are on the way as well. As we approach the end of August, let’s take a look at what September has in store for us. IFA 2023 One of the world’s largest consumer electronics and home appliances trade show, the Internationale Funkausstellung (IFA) 2023 will take place from September 1 to 5 at the Messe Berlin Exhibition Grounds.''', font = "arial 12", justify = LEFT, wraplength = 800)
lb_text2.grid(row = 0, column = 3)

#gap b/w f2 and f3
gap2 = Label(f2, text = "")
gap2.grid(row = 1, column = 0)

# 3rd Frame
f3 = Frame(root)
f3.pack(side = TOP, anchor = "nw", fill = "x")

# shift 3rd pic 
s4 = Label(f3, text = "             ")
s4.grid(row = 0, column = 0)

# News 3
pic3 = Image.open("C:\\Users\\mrank\\OneDrive\\Documents\\###  MY WORKS  ###\\[ BACKEND DEVELOPMENT ]\\[ PYTHON ]\\TKINTER\\7_Exercise_3\\3.png")
resized_pic3 = pic3.resize((350, 200), Image.ANTIALIAS)
new_pic3 = ImageTk.PhotoImage(resized_pic3)
lb_pic3 = Label(f3, image = new_pic3, relief = GROOVE, borderwidth = 10)
lb_pic3.grid(row = 0, column = 1)

# shift 3rd text
s5 = Label(f3, text = "             ")
s5.grid(row = 0, column = 2)

lb_text3 = Label(f3, text = '''New Delhi: The government has called for a "special session of Parliament" to be held from September 18 to 22, Union Minister Pralhad Joshi posted on X (formerly Twitter), adding, that there will be five sittings. "Amid Amrit Kaal, looking forward to having a fruitful discussion and debate in Parliament," he said. Government sources have, so far, been tight-lipped on possible agendas. There is speculation the special session is being called to begin the process of shifting from the old to the new Parliament building. So, this session may begin in the old and end in the new. Also, it may not be a joint session of the Lok Sabha and Rajya Sabha.''', font = "arial 12", justify = LEFT, wraplength = 800)
lb_text3.grid(row = 0, column = 3)


root.mainloop()