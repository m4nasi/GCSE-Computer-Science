def LoadLogin():
    newDB = []
    Login = open("Sorting", "r")
    user = Login.read().splitlines()
    for user in user:
        logins = {}
        users = user.split (",")
        logins["username"] = users[0]
        logins["password"] = int(users[1])
        newDB.append(logins)
    return newDB

def EnterLogin():
    print("Please enter your username:")
    userName = input("?")
    print("Please enter your password:")
    password = input("?")
        
def AddLogin():
    print("What is your name?")
    Name = input("?")
    print("Please enter an username:")
    NewUserName = input("?")
    print("Please enter a password")
    Newpassword = input("?")
    print("Please re-enter password")
    ReenteredPassword = input("?")
    if Newpassword == ReenteredPassword:
        Newpassword = ReenteredPassword
    else:
        print("The password does not match ")
    
#AllWords = LoadDict()
canContinue = True
while (canContinue == True):
    print("Hello!")
    print("Do you want to:")
    print("1: Enter login")
    print("2: Create a new account")
    print("3: Exit")
    choice = input("?")
    choice = choice.upper()
    if choice == "1":
        EnterLogin()
        
    elif choice == "2":
        AddLogin()
        
    elif choice == "3":
        canContinue = False
        
    else:
        print("I do not understand " + choice)
        
#password = password + 1
