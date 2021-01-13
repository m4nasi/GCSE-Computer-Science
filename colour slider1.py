from tkinter import *
###### creates a tkinter window ########
myGUI = Tk()
myGUI.geometry("600x600")
myGUI.title("My layout")
myGUI.configure(bg = "black")
myCanvas = Canvas (myGUI);
myCanvas.pack()
myCanvas.configure(bg = "black")
###### sets the scales so it adds a little bit of the primary colours; blue, red and green #######
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
        
def submit():
    myCanvas.configure(bg = NameText4.get())
##### makes buttons of preset colours #######    
def makeRed():
    myCanvas.configure(bg = "red")

def makeBlue():
    myCanvas.configure(bg = "blue")

def makeYellow():
    myCanvas.configure(bg = "yellow")

def makeGreen():
    myCanvas.configure(bg = "green")

def makePink():
    myCanvas.configure(bg = "pink")

btn_pink = Button(myGUI, text = "pink", command = makePink)
btn_pink.pack()
btn_pink.configure(bg = "pink")
btn_pink.place(x=10, y=10)

btn_green = Button(myGUI, text = "green", command = makeGreen)
btn_green.pack()
btn_green.configure(bg = "green")
btn_green.place(x=10, y=35)

btn_yellow = Button(myGUI, text = "yellow", command = makeYellow)
btn_yellow.pack()
btn_yellow.configure(bg = "yellow")
btn_yellow.place(x=10, y=61)

btn_blue = Button(myGUI, text = "blue", command = makeBlue)
btn_blue.pack()
btn_blue.configure(bg = "blue")
btn_blue.place(x=10, y=85)

btn_red = Button(myGUI, text = "red", command = makeRed)
btn_red.pack()
btn_red.configure(bg = "red")
btn_red.place(x=10, y=110)
##### adds the value given to the chosen scale #######
def submit6():
    Red.set(NameText6.get())
NameLabel6String = StringVar()
NameLabel6String.set("Type a value for the red scale: ")
NameLabel6 = Label (myGUI, textvariable = NameLabel6String)
NameLabel6.pack()
NameLabel6.configure(bg = "red")
NameLabel6.place(x=380, y=270)
NameText6 = Entry (myGUI, bd = 5, width = 20)
NameText6.pack()
NameText6.place(x=380, y=290)
red = Button(myGUI, text = "submit", command = submit6)
red.pack()
red.place(x=380, y=318)
red.configure(bg = "red")
#########################################################################
def submit7():
    Green.set(NameText7.get())
NameLabel7String = StringVar()
NameLabel7String.set("Type a value for the green scale: ")
NameLabel7 = Label (myGUI, textvariable = NameLabel7String)
NameLabel7.pack()
NameLabel7.place(x=380, y=350)
NameLabel7.configure(bg = "green")
NameText7 = Entry (myGUI, bd = 5, width = 20)
NameText7.pack()
NameText7.place(x=380, y=370)
green = Button(myGUI, text = "submit", command = submit7)
green.pack()
green.place(x=380, y=395)
green.configure(bg = "green")
#########################################################################
def submit8():
    Blue.set(NameText8.get())
NameLabel8String = StringVar()
NameLabel8String.set("Type a value for the blue scale: ")
NameLabel8 = Label (myGUI, textvariable = NameLabel8String)
NameLabel8.pack()
NameLabel8.configure(bg = "blue")
NameLabel8.place(x=380, y=420)
NameText8 = Entry (myGUI, bd = 5, width = 20)
NameText8.pack()
NameText8.place(x=380, y=450)
blue = Button(myGUI, text = "submit", command = submit8)
blue.pack()
blue.place(x=380, y=475)
blue.configure(bg = "blue")
###### creates a variable to change the background #####
def submit3():
    def value_chosen(passed_value):
        selection = value.get()
        label.configure(text = selection)
        myRGB = "#%02x%02x%02x" % (Red.get(), Blue.get(), Green.get())
        myGUI.configure(bg = myRGB)
    def value_chosen2(passed_value):
        selection = value2.get()
        label2.configure(text = selection)
        myRGB = "#%02x%02x%02x" % (Red.get(), Blue.get(), Green.get())
        myGUI.configure(bg = myRGB)
        
    def value_chosen3(passed_value):
        selection = value3.get()
        label3.configure(text = selection)
        myRGB = "#%02x%02x%02x" % (Red.get(), Blue.get(), Green.get())
        myGUI.configure(bg = myRGB)
        
    NameLabelString = StringVar()
    NameLabelString.set("Red")
    NameLabel = Label (myGUI, textvariable = NameLabelString)
    NameLabel.place(x=200, y=270)
    value = StringVar()
    Red = Scale(myGUI, from_=0, to=255, orient=HORIZONTAL, command=value_chosen)
    Red.pack()
    Red.place(x=10 ,y=250)
    Red.configure(bg = "red")
    label = Label(myGUI)
    label.pack()

    NameLabel2String = StringVar()
    NameLabel2String.set("Blue")
    NameLabel2 = Label (myGUI, textvariable = NameLabel2String)
    NameLabel2.place(x=200, y=310)
    value2 = StringVar()
    Green = Scale(myGUI, from_=0, to=255, orient=HORIZONTAL, command=value_chosen2)
    Green.pack()
    Green.place(x=10 ,y=300)
    Green.configure(bg = "blue")
    label2 = Label(myGUI)
    label2.pack()

    NameLabel3String = StringVar()
    NameLabel3String.set("Green")
    NameLabel3 = Label (myGUI, textvariable = NameLabel3String)
    NameLabel3.place(x=200, y=360)
    value3 = StringVar()
    Blue = Scale(myGUI, from_=0, to=255, orient=HORIZONTAL, command=value_chosen3)
    Blue.pack()
    Blue.place(x=10 ,y=350)
    Blue.configure(bg = "green")
    label3 = Label(myGUI)
    label3.pack()

    def submit():
        myGUI.configure(bg = NameText4.get())

    NameLabel4String = StringVar()
    NameLabel4String.set("Type a colour :")
    NameLabel4 = Label (myGUI, textvariable = NameLabel4String)
    NameLabel4.pack()
    NameLabel4.place(x=10, y=390)
    NameText4 = Entry (myGUI, bd = 5, width = 20)
    NameText4.pack()
    NameText4.place(x=10, y=415)

    btn_submit = Button(myGUI, text = "submit", command = submit)
    btn_submit.pack()
    btn_submit.place(x=10 , y=445)

btn_submit = Button(myGUI, text = "background", command = submit3)
btn_submit.pack()
btn_submit.place(x=10 , y=200)

###### allows you to choose a colour for the rectangle ######
NameLabel4String = StringVar()
NameLabel4String.set("Type a colour :")
NameLabel4 = Label (myGUI, textvariable = NameLabel4String)
NameLabel4.pack()
NameLabel4.place(x=200, y=400)
NameText4 = Entry (myGUI, bd = 5, width = 20)
NameText4.pack()
NameText4.place(x=200, y=425)

btn_submit = Button(myGUI, text = "submit", command = submit)
btn_submit.pack()
btn_submit.place(x=200 , y=455)

NameLabelString = StringVar()
NameLabelString.set("Red")
NameLabel = Label (myGUI, textvariable = NameLabelString)
NameLabel.place(x=200, y=270)
value = StringVar()
Red = Scale(myGUI, from_=0, to=255, orient=HORIZONTAL, showvalue=0, variable=value, command=value_chosen)
Red.pack()
Red.configure(bg = "red")
label = Label(myGUI)
label.pack()

NameLabel2String = StringVar()
NameLabel2String.set("Blue")
NameLabel2 = Label (myGUI, textvariable = NameLabel2String)
NameLabel2.place(x=200, y=310)
value2 = StringVar()
Green = Scale(myGUI, from_=0, to=255, orient=HORIZONTAL, showvalue=0, variable=value2, command=value_chosen2)
Green.pack()
Green.configure(bg = "blue")
label2 = Label(myGUI)
label2.pack()

NameLabel3String = StringVar()
NameLabel3String.set("Green")
NameLabel3 = Label (myGUI, textvariable = NameLabel3String)
NameLabel3.place(x=200, y=360)
value3 = StringVar()
Blue = Scale(myGUI, from_=0, to=255, orient=HORIZONTAL, showvalue=0, variable=value3, command=value_chosen3)
Blue.pack()
Blue.configure(bg = "green")
label3 = Label(myGUI)
label3.pack()

def submit4():
    myGUI.configure(bg = "black")
    myCanvas.configure(bg = "black")
    Blue.set(0)
    Red.set(0)
    Green.set(0)
    submit3().set(0)
    
btn_submit = Button(myGUI, text = "reset", command = submit4)
btn_submit.pack()
btn_submit.place(x=10 , y=500)
