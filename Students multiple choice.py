def NewFile():
    NewDB = []
    File = open("Questions.csv", "r")
    Fileline = File.read().splitlines()
    for Fileline in Fileline:
        Array = {}
        users = Fileline.split(",")
        Array["Question 1"] = users[0]
        Array["Answer 1"] = users[1]
        Array["Question 2"] = users[2]
        Array["Answer 2"] = users[3]
        Array["Question 3"] = users[4]
        Array["Answer 3"] = users[5]
        NewDB.append(Array)
    return NewDB

def Start():
    for Array in load:
        print(LocalArray["Question 1"])
        print(LocalArray["Answer 1"])
        print("What do you think the answer is?")
        UserNameInput = input("?")
        recordFound = False
        for LocalArray in load:
            if LocalArray["username"] == UserNameInput:
                recordFound = True
                print("Welcome " + LocalArray["username"])
        if recordFound == False:
                print("not correct")

def Questions():
    Continue = True
    while Continue == True:
        for LocalArray in load:
            print("The first question is:")
            print(LocalArray["Question 1"])
            print(LocalArray["Answer 1"])
            UserInput = input("?")
            if UserInput == LocalArray["Answer 1"]:
                print("correct")
                score =+ 1
                run =+ 1
                print("You have " + str(score) + " point")
            else:
                print("incorrect")
                
            print("The second question is:")
            print(LocalArray["Question 2"])
            UserSecondInput = input("?")
            if UserSecondInput == LocalArray["Answer 2"]:
                print("correct")
                score = score + 1
                run =+ 1
                print("You have " + str(score) + " point")
            else:
                print("incorrect")
                
            print("The third question is:")
            print(LocalArray["Question 3"])
            UserThirdInput = input("?")
            if UserThirdInput == LocalArray["Answer 3"]:
                print("correct")
                score = score + 1
                run =+ 1
                print("You have " + str(score) + " point")
            else:
                print("incorrect")
                
            print("You scored " + score + " points")
            Continue = False
                
score = 0
run = 1
load = NewFile()
canContinue = True
while (canContinue == True):
    #print("Hello!")
    print("Do you want to:")
    print("1: Enter login")
    print("2: Create a new account")
    print("3: Exit")
    choice = input("?")
    if choice == "1":
        Questions()
        
    elif choice == "2":
        AddLogin()
        
    elif choice == "3":
        canContinue = False
        print("Ok! Goodbye!")
        
    else:
        print("I do not understand " + choice)

