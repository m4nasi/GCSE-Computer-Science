import random
##### GLOBALS #####
letterGuessed = ""
HangmanHead = " "
HangmanStick = " "
HangmanBody = "    "
HangmanLeg = "    "

theWord = ""
maskWord = ""

#####FUNCTIONS#####
def LoadDict():
    File = open("dictionary.txt","r")
    words = File.read().splitlines()
    return words

def BuildMan():
    if livesleft == 6:
        Head = "  "
        Body = "    "
        Legs = "    "
        if (livesleft == 5):
            Head = " 0"
        elif (livesleft == 4):
            Head = " 0"
            Body = " |  "
        elif (livesleft == 3):
            Head = " 0"
            Body = "/|  "
        elif (livesleft == 2):
            Head = " 0"
            Body = "/|\\ "
        elif (livesleft == 1):
            Head = " 0"
            Body = "/|\\ "
            Legs = "/   "
        elif (livesleft == 0):
            Head = " 0"
            Body = "/|\\ "
            Legs = "/ \\ "
            print ("Sorry you have ran out of lives")
        return Head, Body, Legs
    elif livesleft == 7:
        Stick = "  " 
        Head = "  "
        Body = "    "
        Legs = "    "
        if (livesleft == 6):
            Stick = " |"
        elif (livesleft == 5):
            Stick = " |"
            Head = " 0"
        elif (livesleft == 4):
            Stick = " |"
            Head = " 0"
            Body = " |  "
        elif (livesleft == 3):
            Stick = " |"
            Head = " 0"
            Body = "/|  "
        elif (livesleft == 2):
            Stick = " |"
            Head = " 0"
            Body = "/|\\ "
        elif (livesleft == 1):
            Stick = " |"
            Head = " 0"
            Body = "/|\\ "
            Legs = "/   "
        elif (livesleft == 0):
            Stick = " |"
            Head = " 0"
            Body = "/|\\ "
            Legs = "/ \\ "
            print ("Sorry you have ran out of lives")
        return Head, Body, Legs, Stick
def DrawScreen():
    File = open("dictionary.txt","r")
    Words = File.read()
    words = len(Words.split(" "))
    print("__________________________________________________________________")
    print("|                                       |                        |")
    print("|                                       |                        |")
    print("|             H A N G M A N             |     " + str(words).ljust(6) +  " words       |")
    print("|                                       |                        |")
    print("|---------------------------------------|------------------------|")
    print("|                                       |   ____________________ |")
    print("| "+MaskWord.ljust(26)+"            |   |/        |          |")
    print("|                                       |   |        "+ HangmanStick +"           |")
    print("|                                       |   |        " + HangmanHead + "          |")
    print("| Lives left: "+ str (livesleft) + "                         |   |        " + HangmanBody + "        |")
    print("|                                       |   |        " + HangmanLeg + "        |")
    print("|                                       |   |                    |")
    print("| Letters guessed:  " + str(LettersGuessed.ljust(18)) + "  |   |\__________________ |") 
    print("|                                       |                        |")
    print("|_______________________________________|________________________|")

##### MAIN PROGRAM #####
AllWords = LoadDict()
NoOfWords = len(AllWords)
TheWord = random.choice(AllWords)
MaskWord = "*" * len(TheWord)
print (TheWord)
LettersGuessed = " "
Continue = True
while Continue:
    print ("How many lives do you want?")
    print ("A: 6")
    print ("B: 7")
    print ("C: 8")
    livesLeft = input ("?")
    if livesLeft.lower() == "a":
        livesleft = 6
        Continue = False
    elif livesLeft.lower() == "b":
        livesleft = 7
        Continue = False
    elif livesLeft.lower() == "c":
        livesleft = 8
        Continue = False
    else:
        print ("I don't understand")

gameOn = True
while gameOn:
    HangmanHead, HangmanBody, HangmanLeg = BuildMan()
    DrawScreen()
    print ("Please guess a letter")
    userGuess = input ("?")
    if(len(userGuess)> 1):
        print ("Pick only one letter")
    else: 
        userGuess = userGuess.upper()
        if(LettersGuessed.find(userGuess) >= 0):
            print("Letter already guessed")
        else:
            LettersGuessed += userGuess
            pos =  -1
            if (TheWord.find(userGuess) >= 0):
                while (TheWord.find(userGuess, pos + 1) >= 0 ):  
                    print ("looking from " + str(pos + 1) + " which is " + TheWord [pos + 1])
                    pos = TheWord.find(userGuess, pos + 1 )
                    MaskWord = MaskWord [0:pos] + userGuess + MaskWord [pos + 1 : len(MaskWord)]
                    
                    if (TheWord == MaskWord):
                        gameOn = False
                print ("Well Done!")
            else:
                livesleft -= 1
                if livesleft == 0:
                    gameOn = False
                print ("That letter is not in the word!")
HangmanHead, HangmanBody, HangmanLeg = BuildMan()
DrawScreen()               
if (livesleft == 0):
    print ("You lost, the word was " + TheWord)
else:
    print ("You won! Well done!")
