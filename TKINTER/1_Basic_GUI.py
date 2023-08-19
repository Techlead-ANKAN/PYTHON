# What is GUI ?
# --> GUI stands for Graphical User Interface. It is form of interface that allows user to interact with the computer in an attractive way using visual indicators like icons, menus, windows, buttons, etc.


# What is Tkinter ?
# --> Tkinter is an in-built python module that is used to create GUI applications. It is one of the most commonly used module used for creating GUI applications. It gives an object-oriented interface to the TK GUI toolkit.

# Fundamental structure of Tkinter program (Syntax)
#       ___________________________
#     |                           |
#     | Importing Tkinter modules |
#     | __________________________|                           
#                   |
#                   | 
#                  \/
#    ________________________________________
#  |                                        |
#  |  Creating main window for the GUI app  |
#  | _______________________________________|
#                   |
#                   |
#                  \/
#         ___________________________
#       |                           |
#       | Adding widgets to the app |
#       |___________________________|
#                   |
#                   |
#                  \/
#       ___________________________
#      |                           |
#      | Enter the main event loop |
#      |___________________________|

# example: -

from tkinter import *     # Importing all the modules fromm the Tkinter library


root = Tk()   # An instance, named "root" of class Tk() has been created. 
              # It basically creates the basic GUI(including the basic components of gui that are present in every gui, thus creating a base GUI for you). 

# < GUI Logic(s) here >


root.mainloop()   # Eventloop / Mainloop - it basically checks for any news events over and over again, many times every second. 
                  # It is simply a method in the main window that executes what wish to execute in an application. 
                  # as the name implies it will run forever until the user exits the window or waits for any events from the user.