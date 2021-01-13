def LoadFile():
    newDB = []
    StudentFile = open("Students500.csv", "r")
    StudentRows = StudentFile.read().splitlines()
    for StudentRows in StudentRows:
        StudentDict = {}
        StudentArray = StudentRows.split (",")
        StudentDict["name"] = StudentArray[0]
        StudentDict["age"] = int(StudentArray[1])
        StudentDict["form"] = StudentArray[2]
        newDB.append(StudentDict)
    return newDB

##########################################################################################################
def ViewAllRecord(myLocalDB):
    print ("You are in view all record")
    print ("+--------------------+----+-----+")
    print ("|Name                |Age |Form |")
    print ("+--------------------+----+-----+")
    for LocalStudentDict in myLocalDB:
        StudentName = LocalStudentDict ["name"]
        StudentAge = str(LocalStudentDict ["age"])
        StudentForm = LocalStudentDict ["form"]
        print("|" + StudentName.ljust(20) + "|" + StudentAge.ljust(4)+ "|" + StudentForm.ljust(5)+ "|")
    print ("+--------------------+----+-----+")
    
def ViewATypeRecord(myLocalDB):
    print ("You are in view a type of record")
    print ("Do you want to find out the:")
    print ("A: Name ")
    print ("B: Age ")
    print ("C: Form ")
    print ("Choose: A,B,C")
    userChoice = input ("?")
    if (userChoice.upper() == "A"):
        print ("+--------------------+")
        print ("|Name                |")
        print ("+--------------------+")
        for LocalStudentDict in myLocalDB:
            StudentName = LocalStudentDict ["name"]
            print ("|" + StudentName.ljust(20)+ "|")
        print ("+--------------------+")
        
    elif (userChoice.upper() == "B"):
        print("+----+")
        print("|Age |")
        print("+----+")
        for LocalStudentDict in myLocalDB:
            StudentAge = LocalStudentDict ["age"]
            print ("|" + str(StudentAge) + "  |")
        print("+----+")
        
    elif (userChoice.upper() == "C"):
        print("+-----+")
        print("|Form |")
        print("+-----+")
        for LocalStudentDict in myLocalDB:
            StudentForm = LocalStudentDict ["form"]
            print ("|" + StudentForm.ljust(5)+ "|")
        print("+-----+")
        
    else:
        print ("I do not understand " + userOption)

def BubbleSort(myLocalDB):
    print ("What do you want to sort?")
    print ("A: Name")
    print ("B: Age")
    print ("C: Form")
    userchoice1 = input ("?")
    if userchoice1.lower()== "a":
        print("Names")
        sort = "name"             
    elif userchoice1.lower()== "b":
        print("Ages")
        sort = "age"

    elif userchoice1.lower()== "c":
        print("Forms")
        sort = "form"

    else:
        print ("I do not understand " + userchoice1)
        
    Sorted = False
    while Sorted == False:
        Sorted = True
        for count in range (len(myLocalDB)-1):
            studA = myLocalDB[count]
            studB = myLocalDB[count+1]
            if (studA[sort]>studB[sort]):
                Sorted = False
                Temp = myLocalDB[count]
                myLocalDB[count] = myLocalDB[count+1]
                myLocalDB[count+1] = Temp

def InsertionSort(myLocalDB):
    if len(myLocalDB)==1:
        return myLocalDB
    print ("What do you want to sort?")
    print ("A: Name")
    print ("B: Age")
    print ("C: Form")
    userchoice1 = input ("?")
    if userchoice1.lower()== "a":
        print("Names")
        sort = "name"             
    elif userchoice1.lower()== "b":
        print("Ages")
        sort = "age"

    elif userchoice1.lower()== "c":
        print("Forms")
        sort = "form"

    else:
        print ("I do not understand " + userchoice1)
        
    for count in range (1,len(myLocalDB)):
        countback = count
        while countback > 0 and myLocalDB[countback][sort] < myLocalDB[countback - 1][sort]:
            Temp = myLocalDB[countback]
            myLocalDB[countback] = myLocalDB[countback-1]
            myLocalDB[countback-1] = Temp
            countback -= 1
            
def MergeSort(myLocalDB):
    mergesort = True
    newStudentDB = []
    if len(myLocalDB)==1:
        return myLocalDB

    halfwayPoint = int(len(myLocalDB)/2)
    lowerStudentList = myLocalDB[:halfwayPoint]
    upperStudentList = myLocalDB[halfwayPoint:]
    lowerStudentList = MergeSort(lowerStudentList)
    upperStudentList = MergeSort(upperStudentList)

    lowercount = 0
    uppercount = 0
    while(lowercount < len(lowerStudentList) or uppercount < len(upperStudentList)):
        if (lowercount == len(lowerStudentList)):
            newStudentDB.append(upperStudentList[uppercount])
            uppercount += 1
        
        elif (uppercount == len(upperStudentList)):
            newStudentDB.append(lowerStudentList[lowercount])
            lowercount += 1

        elif(lowerStudentList[lowercount]["name"] < upperStudentList[uppercount]["name"]):
            newStudentDB.append(lowerStudentList[lowercount])
            lowercount += 1

        else:
            newStudentDB.append(upperStudentList[uppercount])
            uppercount += 1
        #print(newStudentDB)
    return newStudentDB
    myLocalDB = newStudentDB
    
def Sort(myLocalDB):
    print ("A: Bubble Sort")
    print ("B: Insertion Sort")
    print ("C: Merge Sort")
    userchoice = input ("?")
    if userchoice.lower()== "a":
        print("Bubble sort")
        BubbleSort(myLocalDB)
                     
    elif userchoice.lower()== "b":
        print("Insertion sort")
        InsertionSort(myLocalDB)

    elif userchoice.lower()== "c":
        print("merge sort")
        myLocalDB = MergeSort(myLocalDB)
    else:
        print ("I do not understand " + userchoice)
        
    return myLocalDB

def ViewARecord(myLocalDB):
    print ("Enter name of record to view")
    userChoice = input ("?")
    recordFound = False
    for LocalStudentDict in myLocalDB:
        if (LocalStudentDict["name"].upper() == userChoice.upper()):
            recordFound = True
            print ("Name: " + LocalStudentDict ["name"])
            print ("Age: " + str(LocalStudentDict ["age"]))
            print ("Form: " + LocalStudentDict ["form"])
            
    if(recordFound == False):
        print ("I do not understand " + userChoice)
    
def Count(myLocalDB):
    StudentDB = LoadFile()
    print("Do you want to count:")
    print("A: names")
    print("B: ages")
    print("C: forms")
    useroption2 = input("?")
    File = open("Students500.csv","r")
    words = File.read()
    if useroption2.lower() == "a":
        print("There are " + str(len(words.split(" "))) + " names")
            
    elif useroption2.lower() == "b":
        print("There are " + str(len(words.split(" "))) + " ages")
            
    elif useroption2.lower() == "c":
        print("There are " + str(len(words.split(" "))) + " forms")

    else:
        print ("I do not understand " + useroption2)

def write(myLocalDB):
    File = open("NewStudents500.csv","w")
    print("What type of record do you want to write?:")
    print("name:")
    newname = input("?")
    StudentDict1 ["name"].append(newname)
    print("age:")
    newage = input("?")
    StudentDict1 ["age"].append(newage)
    print("form:")
    newform = input("?")
    StudentDict1 ["form"].append(newform)
    File.close()
    return myLocalDB
    myLocalDB = myLocalDB

def LoadSecondFile():
    newDB1 = []
    StudentFile1 = open("NewStudents500.csv", "r")
    StudentRows1 = StudentFile1.read().splitlines()
    for StudentRows1 in StudentRows1:
        StudentDict1 = {}
        StudentArray1 = StudentRows1.split (",")
        StudentDict1["name"] = StudentArray[0]
        StudentDict1["age"] = int(StudentArray[1])
        StudentDict1["form"] = StudentArray[2]
        newDB1.append(StudentDict)
    return newDB1

def Read():
    StudentDB1 = LoadSecondFile()
    print ("+--------------------+----+-----+")
    print ("|Name                |Age |Form |")
    print ("+--------------------+----+-----+")
    for LocalStudentDict1 in myLocalDB1:
        StudentName = LocalStudentDict1 ["name"]
        StudentAge = str(LocalStudentDict1 ["age"])
        StudentForm = LocalStudentDict1 ["form"]
        print("|" + StudentName.ljust(20) + "|" + StudentAge.ljust(4)+ "|" + StudentForm.ljust(5)+ "|")
    print ("+--------------------+----+-----+")
####################################################################################################
StudentDB = LoadFile()
canContinue = True
while (canContinue == True):
    print ("A: View all records ")
    print ("B: View a record ")
    print ("C: Sort record ")
    print ("D: A type of record ")
    print ("E: Count ")
    print ("F: Write a record ")
    print ("G: View your written record")
    print ("H: Quit ")
    print ("Choose: A,B,C,D,E,F ")
    userOption = input ("?")
    if (userOption.upper() == "A"):
        ViewAllRecord(StudentDB)
        
    elif (userOption.upper() == "B"):
        ViewARecord(StudentDB)
        
    elif (userOption.upper() == "C"):
        StudentDB = Sort(StudentDB)
        
    elif (userOption.upper() == "D"):
        ViewATypeRecord(StudentDB)

    elif (userOption.upper() == "E"):
        Count(StudentDB)

    elif (userOption.upper() == "F"):
        write(StudentDB)

    elif (userOption.upper() == "G"):
        read(StudentDB)
        
    elif (userOption.upper() == "H"):
        print ("Ok! Goodbye!")
        canContinue = False
    else:
        print ("I do not understand " + userOption)

