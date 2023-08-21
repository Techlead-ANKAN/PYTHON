# Attributes of Label and Pack

from tkinter import *
root = Tk()

''' GUI Logic(s) '''

root.geometry("1920x1080")
root.title("Ankan's GUI")   # sets the title of the GUI

# Attributes of Label: -  (* - common / important)

# *1) text -- Used to set the text as a label
# 2) anchor -- It is used to control the positioning of the text
# *3) bg -- It is used to set the background colour of the label
# 4) height -- It is used to set the vertical dimension of the frame
# 5) width -- It is used to set the width of the label in characters (not pixels). If this option is not set, the label will be sized to fit its contents.
# *6) bd -- It is used to set the size of the border.
# *7) font -- specifies the font
# 8) cursor -- It is used to specify what cursor to show when the it is hovered over the label. (Default - standard cursor)
# 9) textvariable -- As the name suggests it is associated with a Tkinter variable (usually a StringVar) with the label. If the variable is changed, the label text is updated.
# 10) bitmap -- It is used to set the bitmap to the graphical object specified so that, the label can represent the graphics instead of text.
# *11) fg -- The colour of the label(text)
# 12) image -- It is used to display the a static image in the label widget
# *13) padx -- padding in x-driection
# *14) pady -- padding in y-direction
# 15) justify -- it is used to define how to align multiple lines of text. Use LEFT, RIGHT and CENTER as its values.
# *16) relief -- It sets a specific border. SUNKEN, RAISED, GROOVE, RIDGE
# 17) underline -- you can display an underline below the nth character, counting form 0, by setting this option to n. the default is underline = -1, which means no underlining.

# Syntax: - Label(options....)
lb = Label(text = "Ankan is a good boy.", bg = "cyan", fg = "black", padx = 100, pady = 100, font = "arial 20 bold", borderwidth = 5, relief = SUNKEN)

# Attributes of Pack: -

# 1) side -- It is used to set the GUI in which sides - BOTTOM, TOP, LEFT, RIGHT. Default --> TOP
# 2) anchor -- It is used to set the GUI in the spcified position in the side.
# 4) fill -- It is used to expand the label in 2 directions - X and Y. Fill in x-direction is possible only when side = TOP / BOTTOM. Fill in y-direction is possible only when side = LEFT / RIGHT
# 5) padx -- padding in x-driection
# 6) pady -- padding in y-driection

# Syntax: - pack(options....)
lb.pack(side = TOP, anchor = "n", padx = 50, pady =50)

root.mainloop()
