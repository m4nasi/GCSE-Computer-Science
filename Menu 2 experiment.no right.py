def LoadFile():
    newDB = []
    StudentFile = open("Student.csv", "r")
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
            print ("|" + StudentAge.ljust(4)+ "|")
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
        print ("+--------------------+----+-----+")
        print ("|Name                |Age |Form |")
        print ("+--------------------+----+-----+")
        for LocalStudentDict in newStudentDB:
            StudentName = LocalStudentDict ["name"]
            StudentAge = str(LocalStudentDict ["age"])
            StudentForm = LocalStudentDict ["form"]
            print("|" + StudentName.ljust(20) + "|" + StudentAge.ljust(4)+ "|" + StudentForm.ljust(5)+ "|")
        print ("+--------------------+----+-----+")
        mergesort = True
    return newStudentDB

    
def Sort(myLocalDB):
    print ("A: Bubble Sort")
    print ("B: Insertion Sort")
    print ("C: Merge Sort")
    userchoice = input ("?")
    if userchoice.lower()== "a":
        print("Bubble sort")
        BubbleSort(StudentDB)
                     
    elif userchoice.lower()== "b":
        print("Insertion sort")
        InsertionSort(StudentDB)

    elif userchoice.lower()== "c":
        print("merge sort")
        myLocalDB = MergeSort(myLocalDB)
        
    else:
        print ("I do not understand " + userchoice)
    return StudentDB

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
    if useroption2.lower() == "a":
        for LocalStudentDict in myLocalDB:
            StudentName = LocalStudentDict ["name"]
            words = StudentName
            word = len(words.split(" "))
            print("There are " + str(word) + " names")
            
    elif useroption2.lower() == "b":
        for LocalStudentDict in myLocalDB:
            StudentAge = LocalStudentDict ["age"]
            words = StudentAge
            StudentAge = str(LocalStudentDict ["age"])
            word = words.split(" ")
            print("There are " + str(word) + " ages")
            
    elif useroption2.lower() == "c":
        for LocalStudentDict in myLocalDB:
            StudentForm = LocalStudentDict ["form"]
            words = StudentForm
            StudentForm = LocalStudentDict ["form"]
            word = len(words.split(" "))
            print("There are " + str(word) + " forms")

    else:
        print ("I do not understand " + useroption2)

def ViewAllRecord(myLocalDB):
    print ("You are in view all record")
    print ("+--------------------+----+-----+")
    print ("|Name                |Age |Form |")
    print ("+--------------------+----+-----+")
    if mergesort == True:
        myLocalDB = MergeSort(StudentDB)
    for LocalStudentDict in myLocalDB:
        StudentName = LocalStudentDict ["name"]
        StudentAge = str(LocalStudentDict ["age"])
        StudentForm = LocalStudentDict ["form"]
        print("|" + StudentName.ljust(20) + "|" + StudentAge.ljust(4)+ "|" + StudentForm.ljust(5)+ "|")
    print ("+--------------------+----+-----+")
    
####################################################################################################
mergesort = False
StudentDB = LoadFile()
canContinue = True
while (canContinue == True):
    print ("A: View all records ")
    print ("B: View a record ")
    print ("C: Sort record ")
    print ("D: A type of record ")
    print ("E: Count")
    print ("F: quit ")
    print ("Choose: A,B,C,D,E,F ")
    userOption = input ("?")
    if (userOption.upper() == "A"):
        ViewAllRecord(StudentDB)
        
    elif (userOption.upper() == "B"):
        ViewARecord(StudentDB)
        
    elif (userOption.upper() == "C"):
        myLocalDB = Sort(StudentDB)
        
    elif (userOption.upper() == "D"):
        ViewATypeRecord(StudentDB)

    elif (userOption.upper() == "E"):
        Count(StudentDB)
        
    elif (userOption.upper() == "F"):
        print ("Ok! Goodbye!")
        canContinue = False
    else:
        print ("I do not understand " + userOption)

