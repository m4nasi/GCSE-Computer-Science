def Main():
    gameon = True
    while (gameon) == True:
        gameon = False
        print ("A: count words ")
        print ("B: display file ")
        print ("C: quit")
        print ("Choose: A,B or C")
        gameon = False
        userOption = input ("?")
        if (userOption.upper() == "A"):
            countWords()
            gameon = False
        elif (userOption.upper() == "C"):
            print ("Goodbye!")
            gameon = False
        else:
            print ("I do not understand " + userOption)

        
def countWords():
    print ("I am in count words")
    continues = True
    while (continues == True):
        print ("Would you like to count a specific word?")
        print ("Yes or No")
        userInput = input ("?")       
        if (userInput.lower()== "yes"):            
            File = open("great expectations.txt","r")
            words = File.read()
            print ("What is the word you want to find?")
            userWord = input ("?")
            specificWord = words.count(userWord)
            if (specificWord == 1):
                print ("There is " + str(specificWord) + " " + (userWord) + " in the whole text")
            else:
                print("There are " + str(specificWord) + " " + (userWord) + "'s in the whole text")
            
            Main()

######################################################
Main()
