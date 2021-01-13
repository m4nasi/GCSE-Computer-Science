from tkinter import *

def value_chosen(passed_value):
    selection = "Value " + value.get()
    label.configure(text = selection)
    myRGB = "#%02x%02x%02x" % (Red.get(), Blue.get(), Green.get())

def value_chosen2(passed_value):
    selection = "Value " + value2.get()
    label.configure(text = selection)
    myRGB = "#%02x%02x%02x" % (Red.get(), Blue.get(), Green.get())

def value_chosen3(passed_value):
    selection = "Value " + value3.get()
    label.configure(text = selection)
    myRGB = "#%02x%02x%02x" % (Red.get(), Blue.get(), Green.get())
    
myGUI = Tk()
myGUI.geometry("300x300")
myGUI.title("My layout")

NameLabelString = StringVar()
NameLabelString.set("Red")
NameLabel = Label (myGUI, textvariable = NameLabelString)
NameLabel.place(x=10, y=10)
value = StringVar()
Red = Scale(myGUI, from_=0, to=255, orient=HORIZONTAL, showvalue=0, variable=value, command=value_chosen)
Red.pack()
label = Label(myGUI)
label.pack()

NameLabelString = StringVar()
NameLabelString.set("Green")
NameLabel = Label (myGUI, textvariable = NameLabelString)
NameLabel.place(x=10, y=45)
value2 = StringVar()
Green = Scale(myGUI, from_=0, to=255, orient=HORIZONTAL, showvalue=0, variable=value, command=value_chosen2)
Green.pack()
label2 = Label(myGUI)
label2.pack()

NameLabelString = StringVar()
NameLabelString.set("Blue")
NameLabel = Label (myGUI, textvariable = NameLabelString)
NameLabel.place(x=10, y=85)
value3 = StringVar()
Blue = Scale(myGUI, from_=0, to=255, orient=HORIZONTAL, showvalue=0, variable=value, command=value_chosen3)
Blue.pack()
label3 = Label(myGUI)
label3.pack()

myGUI.mainloop()
