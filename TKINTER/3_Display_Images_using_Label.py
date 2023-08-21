# Displaying images as a Label using  --->  PhotoImage
# Types of file formats supported by Tkinter PhotoImage: - GIF, PGM, PPM, PNG
 

from tkinter import *

root = Tk()

''' GUI Logic(s)'''

root.geometry("1500x1700")  # setting the dimension of the GUI

# PhotoImage widget -  This widget takes a picture as an arguement and displays them on the GUI.
# syntax: -  < variable >  =  PhotoImage(file = "path\\to\\image")    
pic = PhotoImage(file = "C:\\Users\\mrank\\OneDrive\\Documents\\###  MY WORKS  ###\\[ BACKEND DEVELOPMENT ]\\[ PYTHON ]\\TKINTER\\mypic.png")

lb = Label(image = pic)  # using the picture as a label 

lb.pack()  # packing the label so that it gets displayed in the GUI.

root.mainloop()



# PIL or Pillow Package
# PIL ---> 1) It stands for Python Imaging Library. It provides a way to process images in a program.
#          2) It supports a wide range of image file formats including png, jpeg and gif.
#          3) Basic image processing and manipulation functionability
#          4) Width and height options that can be used to set the Label size for an image. If a size is not specified, the Label will be just large enough to display its contents.

# Note: - pip install pillow


from tkinter import *
from PIL import Image, ImageTk    

root = Tk()

root.geometry("1000x600")

pic = Image.open("C:\\Users\\mrank\\OneDrive\\Documents\\###  MY WORKS  ###\\[ BACKEND DEVELOPMENT ]\\[ PYTHON ]\\TKINTER\\place.jpg")  # opens the image

photo = ImageTk.PhotoImage(pic)   # Manipulates and opens the jpg picture 

lb = Label(image = photo)
lb.pack()

root.mainloop()