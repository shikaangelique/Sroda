import time
from tkinter import *

root = Tk()
root.geometry("500x300")

bloop = Tk()
bloop.geometry("250x150")

# defines the command that is executed after the submit button is pushed
def getvals():
    print("Accepted")
    time.sleep(2)
    root.destroy()

    messie = Label(bloop, text="ACCEPTED")
    messie.grid(row=9, column=3)
    bloop.mainloop()


# Heading
Label(root, text="Sheeks' Form", font="arial 15 bold").grid(row=0, column=3)

# Field names
wee = Label(root, text="Wagymimi?")
waa = Label(root, text="Wabodam?")
wii = Label(root, text="Woyare?")

# Packing fields
wee.grid(row=1, column=2)
waa.grid(row=2, column=2)
wii.grid(row=3, column=2)

# Variables for storing data
weevalue = StringVar
waavalue = StringVar
wiivalue = StringVar
checkvalue = IntVar

# Creating entry fields
weeentry = Entry(root, textvariable=weevalue)
waaentry = Entry(root, textvariable=waavalue)
wiientry = Entry(root, textvariable=wiivalue)

# Packing entry fields
weeentry.grid(row=1, column=3)
waaentry.grid(row=2, column=3)
wiientry.grid(row=3, column=3)

# Creating checkbox
check_button = Checkbutton(text="anaa?", variable=checkvalue)
check_button.grid(row=6, column=3)

# Submit button
Button(text="Submit", command=getvals).grid(row=7, column=3)


root.mainloop()


# To create an executable, install pyinstaller and run
# pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':"tk'
# --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':"tcl' twokintering.py
# ""

#pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk'--add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' twokintering.py