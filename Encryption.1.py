def LoadFile():
    newDB = []
    Usernames = open("Usernames.csv", "r")
    userRows = Usernames.read().splitlines()
    for userRows in userRows:
        UserDict = {}
        userArray = userRows.split (",")
        UserDict["username"] = userArray[0]
        UserDict["password"] = userArray[1]
        newDB.append(UserDict)
    return newDB

def EnterLogin(mylocalDB):
    print("Please enter your username:")

def AddLogin(myLocalDB):
    print("What is your name?")
    
UserDB = LoadFile()
canContinue = True
while (canContinue == True):
    print("Hello!")
    print("Do you want to:")
    print("1: Enter login")
    print("2: Create a new account")
    print("3: Exit")
    choice = input("?")
    if choice == "1":
        EnterLogin(UserDB)
        
    elif choice == "2":
        AddLogin(UserDB)
        
    elif choice == "3":
        canContinue = False
        print("Ok! Goodbye!")
        
    else:
        print("I do not understand " + choice)
