from tkinter import *
def value_chosen(passed_value):
    selection = "Value " + value.get()
    label.configure(text = selection)
    myRGB = "#%02x%02x%02x" % (Red.get(), Blue.get(), Green.get())
    myCanvas.configure(bg = myRGB)
def value_chosen2(passed_value):
    selection = "Value " + value2.get()
    label2.configure(text = selection)
    myRGB = "#%02x%02x%02x" % (Red.get(), Blue.get(), Green.get())
    myCanvas.configure(bg = myRGB)
    
def value_chosen3(passed_value):
    selection = "Value " + value3.get()
    label3.configure(text = selection)
    myRGB = "#%02x%02x%02x" % (Red.get(), Blue.get(), Green.get())
    myCanvas.configure(bg = myRGB)
    
myGUI = Tk()
myGUI.geometry("600x600")
myGUI.title("My layout")

myCanvas = Canvas (myGUI);
myCanvas.pack()

NameLabelString = StringVar()
NameLabelString.set("Red")
NameLabel = Label (myGUI, textvariable = NameLabelString)
NameLabel.place(x=200, y=265)
value = StringVar()
Red = Scale(myGUI, from_=0, to=255, orient=HORIZONTAL, showvalue=0, variable=value, command=value_chosen)
Red.pack()
label = Label(myGUI)
label.pack()

NameLabel2String = StringVar()
NameLabel2String.set("Green")
NameLabel2 = Label (myGUI, textvariable = NameLabel2String)
NameLabel2.place(x=200, y=310)
value2 = StringVar()
Green = Scale(myGUI, from_=0, to=255, orient=HORIZONTAL, showvalue=0, variable=value2, command=value_chosen2)
Green.pack()
label2 = Label(myGUI)
label2.pack()

NameLabel3String = StringVar()
NameLabel3String.set("Blue")
NameLabel3 = Label (myGUI, textvariable = NameLabel3String)
NameLabel3.place(x=200, y=360)
value3 = StringVar()
Blue = Scale(myGUI, from_=0, to=255, orient=HORIZONTAL, showvalue=0, variable=value3, command=value_chosen3)
Blue.pack()
label3 = Label(myGUI)
label3.pack()
