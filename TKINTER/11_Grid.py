# Grid in Tkinter
# The master GUI is split into a no.of rows and columns that can hold widgets. The grid geometry manager puts the widget in a 2 dimensional table.

# Syntax: -
# < widget >.grid(master, options)


# Attributes of grid: -
# 1) column -- specifies the column
# 2) columnspan -- 


from tkinter import *

root = Tk()
root.geometry("400x400")

user = Label(root, text = "UserId")
user.grid(row = 0, column = 0)

password = Label(root, text = "Password")
password.grid(row = 1, column = 0)


userval = StringVar()
passval = StringVar()

userentry = Entry(root, textvariable = userval)
userentry.grid(row = 0, column = 1,)

passentry = Entry(root, textvariable = passval)
passentry.grid(row = 1, column = 1)

sub_button = Button(root, text = "Submit", bg = "cyan", fg = "black", height = 1, width = 9, relief = RIDGE)
sub_button.grid(row = 2, column = 1, sticky = "w")

root.mainloop()