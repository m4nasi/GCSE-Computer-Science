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
    continue1 = True
    while continue1 == True:
        ###asks me what my username is
        print("Please enter your username:")
        userName = input("?")
        recordFound1 = False
        ###searches the database
        for LocalUserDict in UserDB:
            ###sees if the computer can find 
            if (LocalUserDict["username"].upper() == userName.upper()):
                recordFound = True
                ###asks for the password
                print("Please enter your password:")
                password = input("?")
                recordFound1 = True
                ###looks for the password
                if (LocalUserDict["password"].upper() == password.upper()):
                    recordFound1 = False
                    
                continue1 = False
        else:
            print("The username you have entered is invalied. Please try again.")
            continue1 = True
            
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
