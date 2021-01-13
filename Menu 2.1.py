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

def ViewAllRecord(myLocalDB):
    print ("You are in view all record")
    print ("+---------------+----+-----+")
    print ("|Name           |Age |Form |")
    print ("+---------------+----+-----+")
    for LocalStudentDict in myLocalDB:
        StudentName = LocalStudentDict ["name"]
        StudentAge = str(LocalStudentDict ["age"])
        StudentForm = LocalStudentDict ["form"]
        print("|" + StudentName.ljust(15) + "|" + StudentAge.ljust(4)+ "|" + StudentForm.ljust(5)+ "|")
    print ("+---------------+----+-----+")
    
def ViewATypeRecord(myLocalDB):
    print ("You are in view a type of record")
    print ("Do you want to find out the:")
    print ("A: Name ")
    print ("B: Age ")
    print ("C: Form ")
    print ("Choose: A,B,C")
    userChoice = input ("?")
    if (userChoice.upper() == "A"):
        for LocalStudentDict in myLocalDB:
            StudentName = LocalStudentDict ["name"]
            print (StudentName)
        
    elif (userChoice.upper() == "B"):
        for LocalStudentDict in myLocalDB:
            StudentAge = LocalStudentDict ["age"]
            print (StudentAge)
        
    elif (userChoice.upper() == "C"):
        for LocalStudentDict in myLocalDB:
            StudentForm = LocalStudentDict ["form"]
            print (StudentForm)
            
    else:
        print ("I do not understand " + userOption)
    
def Sort(myLocalDB):
    print ("You are in sort")

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


StudentDB = LoadFile()

canContinue = True
while (canContinue == True):
    
    print ("A: View all records ")
    print ("B: View a record ")
    print ("C: Sort record")
    print ("D: quit")
    print ("Choose: A,B,C,D")
    userOption = input ("?")
    
    if (userOption.upper() == "A"):
        ViewAllRecord(StudentDB)
    elif (userOption.upper() == "B"):
        ViewARecord(StudentDB)
    elif (userOption.upper() == "C"):
        Sort(StudentDB)
    elif (userOption.upper() == "D"):
        canContinue = False
    else:
        print ("I do not understand " + userOption)

