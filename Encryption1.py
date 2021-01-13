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
        print("Please enter your username:")
        userName = input("?")
        recordFound = False
        for LocalUserDict in UserDB:
            if (LocalUserDict["username"] == userName):
                recordFound = True
                print("Please enter your password:")
                password = input("?")
                recordFound1 = True
                
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
            
def Encrypt(ReEnteredPassword + 2):
    ciphertext = ""
    for letter in ReEnteredPassword:
    letter = ord(letter)-65
    ciphertext = char(letter) % 26
    return ciphertext

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
        ReEnteredPassword = Encrypt()
        Usernames1 = open("Students.csv", "a", newline = '')
        mydata = username + "," + ReEnteredPassword
        Usernames1.write(mydata) 
        return Usernames1
        print("Welcome " + username)
    else:
        print("N/A")
        
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
        Usernames1 = EnterLogin()
        
    elif choice == "2":
        AddLogin()
        
    elif choice == "3":
        canContinue = False
        print("Ok! Goodbye!")
        
    else:
        print("I do not understand " + choice)
