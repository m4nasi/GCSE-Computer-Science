def LoadFile():
    newDB = []
    Usernames = open("Students.csv", "r")
    userRows = Usernames.read().splitlines()
    for userRows in userRows:
        UserDict = {}
        userArray = userRows.split (",")
        UserDict["username"] = userArray[0]
        UserDict["password"] = userArray[1]
        newDB.append(UserDict)
    return newDB

def EnterLogin():
    continue1 = True
    while continue1 == True:
        ###asks me what my username is
        print("Please enter your username:")
        userName = input("?")
        recordFound = False
        ###searches the database
        for LocalUserDict in UserDB:
            ###sees if the computer can find 
            if (LocalUserDict["username"] == userName):
                recordFound = True
                ###asks for the password
                print("Please enter your password:")
                password = input("?")
                recordFound1 = True
                
                ###looks for the password
                if (LocalUserDict["password"] == password):
                    recordFound1 = False
                    print("Welcome " + userName)
                    continue1 = False
                else:
                    print("The password in incorrect. Try again")
                    continue1 = True
                    
        if (recordFound == False):
            print("The username you have entered is invalid. Please try again.")
            continue1 = True
                
def AddLogin():
    print("What is your name?")
    name = input("?")
    print("What do you want your username to be?")
    username = input("?")
    print("What do you want your password:")
    password = input("?")
    print("Please re enter your password")
    ReEnteredPassword = input("?")
    if password == ReEnteredPassword:
        userRows = Usernames.read().splitlines()
        for userRows1 in userRows1:
            UserDict1 = {}
            mydata = [(ReEnteredPassword), (username)]
            Usernames = open("Students.csv", "w")
            UserDict["username"] = username
            UserDict["password"] = ReEnteredPassword
          
            Usernames.append(UserDict)
            return Usernames
        ("Welcome " + username)
    else:
        print("N/A")
        
def AddLogina():
    userUser = input("Input a username you will be using.")
    userPass = input("Input a password you will be using.")
    myData = [(userUser), (userPass)]
    myFile = open('Students.csv','a',newline='')
    with (myFile):
        writer = myFile.writer(myFile)
        writer.writerows([myData])

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
        EnterLogin()
        
    elif choice == "2":
        AddLogin()
        
    elif choice == "3":
        canContinue = False
        print("Ok! Goodbye!")
        
    else:
        print("I do not understand " + choice)
