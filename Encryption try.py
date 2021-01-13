import csv
def AddLogin():
    userUser = input("Input a username you will be using.")
    userPass = input("Input a password you will be using.")
    myData = [(userUser), (userPass)]
    myFile = open('Students.csv','a',newline='')
    with (myFile):
        writer = myFile.writer(myFile)
        writer.writerows([myData])
        
canContinue = True
while (canContinue == True):
    print("Hello!")
    print("Do you want to:")
    print("1: Enter login")
    print("2: Create a new account")
    print("3: Exit")
    choice = input("?")
    if choice == "1":
        #EnterLogin()
        print("yo")
    elif choice == "2":
        AddLogin()
            
    elif choice == "3":
        canContinue = False
        print("Ok! Goodbye!")
            
    else:
        print("I do not understand " + choice)

