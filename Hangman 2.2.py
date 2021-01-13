import random
##### GLOBALS #####
LettersGuessed = ""
HangmanHead = " "
HangmanBody = "    "
HangmanLeg = "    "
Clue = ""
clues = ""
theWord = ""
maskWord = ""
livesleft = " "
Player1 = ""
Player2 = ""
#####FUNCTIONS#####
def LoadDict():
    File = open("dictionary.txt","r")
    words = File.read().splitlines()
    return words

def BuildMan():
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
    
def DrawScreen1():
    File = open("dictionary.txt","r")
    Words = File.read()
    words = len(Words.split(" "))
    print("__________________________________________________________________")
    print("|                                       |                        |")
    print("|                                       |                        |")
    print("|             H A N G M A N             |       178691 words     |")
    print("|                                       |                        |")
    print("|---------------------------------------|------------------------|")
    print("|                                       |   ____________________ |")
    print("| "+ MaskWord.ljust(26) +"            |   |/        |          |")
    print("| " + Player1.ljust(10) + " has " + str(Player1_lives) + " lives                |   |        " + HangmanHead + "          |")
    print("| " + Player2.ljust(10) + " has " + str(Player2_lives) + " lives                |   |        " + HangmanBody + "        |")
    print("|                                       |   |        " + HangmanLeg + "        |")
    print("|                                       |   |                    |")
    print("| Letters guessed: " + str(LettersGuessed.ljust(18)) + "   |   |\__________________ |") 
    print("|                                       |                        |")
    print("|_______________________________________|________________________|")
#########################################################
AllWords = LoadDict()
NoOfWords = len(AllWords)
TheWord = random.choice(AllWords)
MaskWord = "*" * len(TheWord)
LettersGuessed = " "
print ("Do you want to play hangman?")
playAgain = input("?")
playAgain = playAgain.lower()
while playAgain == "yes":
    Continues = True
    while Continues:
        print ("How many lives does player 1 want?")
        print ("A: 4")
        print ("B: 5")
        print ("C: 6")
        livesLeft = input ("?")
        if livesLeft.lower() == "a":
            Player1_lives = 4
            Continues = False
        elif livesLeft.lower() == "b":
            Player1_lives = 5
            Continues = False
        elif livesLeft.lower() == "c":
            Player1_lives = 6
            Continues = False
        else:
            print ("I don't understand")
            Continues = True
    Continues1 = True
    while Continues1:
        print ("How many lives does player 2 want?")
        print ("A: 4")
        print ("B: 5")
        print ("C: 6")
        livesLeft = input ("?")
        if livesLeft.lower() == "a":
            Player2_lives = 4
            Continues1 = False
        elif livesLeft.lower() == "b":
            Player2_lives = 5
            Continues1 = False
        elif livesLeft.lower() == "c":
            Player2_lives = 6
            Continues1 = False
        else:
            print ("I don't understand")
            Continues1 = True
    playAgain1 = True
    print("What is player one's name?")
    Player1 = input("?")
    print("What is player two's name?")
    Player2 = input ("?")
    players = [Player2, Player1]
    Players = random.choice(players)
    print (Players + " is going first!")
    gameOn = True
    while gameOn:
        HangmanHead, HangmanBody, HangmanLeg = BuildMan()
        DrawScreen1()
        print ("""Please guess a letter.
You can type clue for a hint!
You can also type new for a new word!
If you know the word you can type it completly!""")
        userGuess = input ("?")
        userGuess = userGuess.upper()
        if(len(userGuess)> 1):
            print ("Pick only one letter")
        else: 
            if(LettersGuessed.find(userGuess) >= 0):
                print("Letter already guessed")
            else:
                LettersGuessed += userGuess
                pos =  -1
                if (TheWord.find(userGuess) >= 0):
                    while (TheWord.find(userGuess, pos + 1) >= 0 ):  
                        pos = TheWord.find(userGuess, pos + 1 )
                        MaskWord = MaskWord [0:pos] + userGuess + MaskWord [pos + 1 : len(MaskWord)]  
                        if (TheWord == MaskWord):
                            gameOn = False
                    print ("Well Done!")
                else:
                    if Players == Player2:
                       Player2_lives -= 1
                    elif Players == Player1:
                       Player1_lives -= 1 
                    if livesleft == 0:
                        gameOn = False
                    print ("The letter you have entered is not the word!")
    HangmanHead, HangmanBody, HangmanLeg = BuildMan()
    DrawScreen1()               
    if (livesleft == 0):
        print ("You lost, the word was " + TheWord)
    else:
        print ("You won! Well done!")
    play = True
    while play:
        print ("Do you want to continue?")
        PlayAgain = input ("?")
        PlayAgain = PlayAgain.lower()
        if PlayAgain == "yes":
            AllWord = LoadDict()
            NoOfWord = len(AllWord)
            TheWord1 = random.choice(AllWord)
            TheWord = TheWord1
            MaskWords = "*" * len(TheWord1)
            MaskWord = MaskWords
            LettersGuesseds = ""
            LettersGuessed = LettersGuesseds
            play = False
            playAgain1 = True
                
        if PlayAgain == "no":
            print ("Ok bye!")
            play = False
            playAgain1 = False
            playAgain = False
        else:
            print ("I don't understand!")
            play = True
if playAgain == "no":
    print ("Ok bye!")
    playAgain = False
