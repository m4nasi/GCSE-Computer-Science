def LoadLogin():
    loginDB = []
    FilePointer = open("Usernames.csv", "r")
    FileLines = FilePointer.read().splitlines()
    for FileLines in FileLines:
        Cells = line.split(",")
        loginDB.append(Cells)
    return loginDB

def SaveLogins(loginDB):
    FilePointer = open("Usernames.csv", "w")
    for FileLines in FileLines:
        FilePointer.write(line[0] + "," + line[1])
        FilePointer.close()

def CreateUser(loginDB):
    print("What is your name?")
    Name = input("?")
    print("What do you want your username to be " + Name)
    NewuserName = input("?")
    continue1 = True
    while continue1 == True:
        print("Please enter your password:")
        Newpassword = input("?")
        print("Please re-enter your password:")
        ReEnteredPassword = input("?")
        if ReEnteredPassword == Newpassword:
            Usernames = open("Usernames.csv", "w")
            
            print("Thank you! You may login with the username and password")
            continue1 = False
        else:
            print("Your password does not match, please try again")
            continue1 = True
########################################
activeUser = "No user"
loginDB = LoadLogin()
canContinue = True
while canContinue == True:
    print("User currently logged in is: " + activeUser)
    print("Would you like to:")
    print("1: Create new user")
    print("2: Login")
    print("3: Exit")
    userChoice = input("?")
    if userChoice == "1":
        activeUser = CreateUser(loginDB)
    elif userChoice == "2":
        activeUser = LoadLogin()
    elif userChoice == "3":
        canContinue = False
        SaveLogins(loginDB)
    else:
        print("I don't understand " + userChoice + " please try again")

        
