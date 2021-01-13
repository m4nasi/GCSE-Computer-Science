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

def InsertFile():
    secondDB = []
    Cards = open("Cards.csv", "r")
    cardsRows = Cards.read().splitlines()
    for cardsRows in cardsRows:
        CardsDict = {}
        cardsArray = cardsRows.split (",")
        CardsDict["username"] = cardsArray[0]
        CardsDict["password"] = cardsArray[1]
        secondDB.append(CardsDict)
    return secondDB

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

def Encrypt(ReEnteredPassword):
    ciphertext = ""
    for letter in ReEnteredPassword:
        letter = ord(letter)-65
        letter = letter % 26
        ciphertext = chr(letter) 
    return ciphertext

##############################
UserDB = LoadFile()
CardsDB = InsertFile()
print("Hello")
EnterLogin()
print("loop")
    
