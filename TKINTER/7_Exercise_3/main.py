'''
Task - There are many images (png) in a directory, and the no.of images are given to you and corresponding to that images ther are some news regarding that image. So what we have to do is create a newspaper GUI with it.
'''

from tkinter import *
from PIL import Image, ImageTk


root = Tk()

''' GUI Logic(s) '''

root.geometry("1920x1080+0+0")
root.title("Newspaper")

header_label = Label(text = "Welcome to News Today", bg = "black",fg = "white", font = "arial 20 bold", relief = SUNKEN)
header_label.pack(side = TOP, anchor = "n")

date_label = Label(text = "21.08.2023", font = "robota 10")
date_label.pack(side = TOP, anchor = "n")

# News 1
pic1 = PhotoImage(file = "C:\\Users\\mrank\\OneDrive\\Documents\\###  MY WORKS  ###\\[ BACKEND DEVELOPMENT ]\\[ PYTHON ]\\TKINTER\\7_Exercise_3\\1.png")
lb_pic1 = Label(image = pic1, relief = GROOVE, borderwidth=10)
lb_pic1.pack(side = LEFT, anchor = 'n',pady = 30, padx = 20)

# file1 = open("1.txt", "r")
# text1 = file1.read()
lb_text1 = Label(text = '''Chandrayaan-3 LIVE Updates: ISRO on Monday said a two-way communication between the Chandrayaan-2 orbiter and Chandrayaan-3's lander module has been established.
Chandrayaan-3 was launched from the Satish Dhawan Space Centre in Sriharikota on July 14. (Twitter/Isro)
Chandrayaan-3 was launched from the Satish Dhawan Space Centre in Sriharikota on July 14. (Twitter/Isro)
"‘Welcome, buddy!’ Ch-2 orbiter formally welcomed Ch-3 LM. Two-way communication between the two is established. MOX has now more routes to reach the LM," the space agency said in a post on X (formerly Twitter).
On Sunday,  ISRO announced that the lander module of Chandrayaan-3, the third lunar mission of India, is expected to touch down on the surface of the Moon around 6.04 pm on August 23.
The live telecast of the landing event will begin at 5.20 pm on Wednesday (August 23).
"The soft landing of Chandrayaan-3 is a monumental moment that not only fuels curiosity but also sparks a passion for exploration within the minds of our youth," the ISRO said on X (formally Twitter).''', font = "arial 12", justify = LEFT, wraplength = 1000)
lb_text1.pack(anchor = "n", pady = 45, padx = 20)



# News 2


pic2 = Image.open("C:\\Users\\mrank\\OneDrive\\Documents\\###  MY WORKS  ###\\[ BACKEND DEVELOPMENT ]\\[ PYTHON ]\\TKINTER\\7_Exercise_3\\2.png")
resized_pic2 = pic2.resize((400, 300), Image.ANTIALIAS)
new_pic2 = ImageTk.PhotoImage(resized_pic2) 
lb_pic2 = Label(image = new_pic2, relief = GROOVE, borderwidth = 10)
lb_pic2.pack(side = TOP, anchor = "w", pady = 100) 



root.mainloop()