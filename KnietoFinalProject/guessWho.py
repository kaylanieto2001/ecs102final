##/*  Guess Who
##guessWho.py
##Kayla Nieto
##M3
##Knieto*/

from graphics import*
from random import randrange

#function to create the window
def window():
    #(GW)
    win = GraphWin("Guess Who",1200,800)
    win.setCoords(0,0,1200,800)
    win.setBackground(color_rgb(219, 219, 219))
    return win

#function that creates window at start and then runs the welcome screen to start the user interaction
def createScreen():
    win = window()
    main(win)
    
#Function serves as the welcome screen when you run the program. It waits for a click of one of the three buttons before running another function
def main(win): 
    gw = Text(Point(600,600),"Guess Who!")
    gw.setSize(36)
    gw.draw(win)
    
    playButton = Rectangle(Point(500,450),Point(700,520))
    playButton.setFill("green")
    playButton.draw(win)
    
    playText = Text(Point(600,485),"Play")
    playText.setSize(26)
    playText.draw(win)

    htpButton = Rectangle(Point(500,360),Point(700,430))
    htpButton.setFill("red")
    htpButton.draw(win)

    htpText = Text(Point(600,395),"How to Play")
    htpText.setSize(24)
    htpText.draw(win)

    hsRectangle = Rectangle(Point(500,270),Point(700,340))
    hsRectangle.setFill("yellow")
    hsRectangle.draw(win)

    hsText = Text(Point(600,305),"High Scores")
    hsText.setSize(24)
    hsText.draw(win)
    
    while True:
        #(IMS) 
        click = win.getMouse()
        if checkClick(click,Point(500,450),Point(700,520)) == "clicked":
            clear(win)
            #(FNC)
            main2(win)
            
        elif checkClick(click,Point(500,360),Point(700,430)) == "clicked":
            clear(win)
            htpScreen(win)
            
        elif checkClick(click,Point(500,270),Point(700,340)) == "clicked":
            clear(win)
            highScore(win)

            
#Function that asks for username of the player and waits for submit click then returns it in uppercase form           
def enterUser(win):
    text = Text(Point(600,700),"Please enter 3 letters to save your score.")
    text.setSize(30)
    text.draw(win)
    
    name = Entry(Point(600,600),4)
    name.setSize(36)
    name.draw(win)
    
    play = Rectangle(Point(550,500),Point(650,550))
    play.setFill("pink")
    play.draw(win)
    
    playT = Text(Point(600,525),"Enter")
    playT.setSize(20)
    playT.draw(win)
    
    x= True
    while x ==True:
        click = win.getMouse()
        #(IEB)
        n = name.getText()
        if checkClick(click,play.getP1(),play.getP2()) == "clicked":
            if len(n) == 3:
                clear(win)
                n = n.upper()
                x = False
    return n


#function that displays current high scores without user's score. (This happens before the game starts)               
def highScore(win):
    hs = Text(Point(600,700),"High Scores:")
    hs.setSize(36)
    hs.draw(win)
    highscores = []
    #(IFL) 
    infile = open("highscore.txt","r")
    
    for line in infile:
        line = line.split("\n")
        line = line[0].split(",")
        name = line[0]
        score = int(line[1])
        highscores.append((name, score))
        
    highscores.sort(key=lambda s: s[1])
    
    x = 650
    total = 0
    
    for name,score in highscores:
        if total < 6:
            score = Text(Point(600,x),"{0:.<30}{1}".format(name,score))
            score.setSize(24)
            score.draw(win)
            x = x-60
            total = total+1
            
    HomeButton = Rectangle(Point(480,250),Point(730,310))
    HomeButton.setFill("yellow")
    HomeButton.draw(win)
    
    HomeText = Text(Point(605,280),"Home")
    HomeText.setSize(24)
    HomeText.draw(win)
    
    while True:
        click = win.getMouse()
        if checkClick(click,Point(480,250),Point(730,310)) == "clicked":
            clear(win)
            main(win)

#Function that takes the user's three letter name and updates the high score list using highscore.txt file to add the name and resort the list.  
def updateScores(win,user,guesses):
    #(OTXT) (User is from entry box)
    state = Text(Point(600,700),"{0}{1}{2}".format("Congrats ",user,"! You guessed the correct answer"))
    state.setSize(24)
    state.draw(win)
    
    hs = Text(Point(600,650),"High Scores:")
    hs.setSize(36)
    hs.draw(win)
    guesses = guesses-3
    highscores = []
    #(IFL) 
    infile = open("highscore.txt","r+")
    
    for line in infile:
        line = line.split("\n")
        line = line[0].split(",")
        name = line[0]
        score = int(line[1])
        highscores.append((name, score))
        
    highscores.append((user,guesses))
    highscores.sort(key=lambda s: s[1])
    
    x = 600
    total = 0
    infile.close()
    #(OFL)
    outfile = open("highscore.txt","w+")
    for name,score in highscores:
        nameS = str(name)
        scoreS = str(score)
        print(nameS+","+scoreS,file = outfile)
        if total < 6:
            score = Text(Point(600,x),"{0:.<30}{1}".format(name,score))
            score.setSize(24)
            score.draw(win)
            x = x-60
            total = total+1
            
    quitB = Rectangle(Point(480,190),Point(730,260))
    quitB.setFill("red")
    quitB.draw(win)
    
    quitT = Text(Point(605,225),"Quit")
    quitT.setSize(24)
    quitT.draw(win)
    
    true = True
    while true == True:
        click = win.getMouse()
        if checkClick(click,Point(480,190),Point(730,260)) == "clicked":
            outfile.close()
            true = False
    win.close()
            
#Function to create pop up attributes screen for helpful hints       
def attributes(win,questionBox):
    cover = Rectangle(Point(0,0),Point(1200,800))
    cover.setFill(color_rgb(219, 219, 219))
    cover.draw(win)
    
    closeButton = Rectangle(Point(510,170),Point(690,230))
    closeButton.setFill("red")
    closeButton.draw(win)
    
    closeText = Text(Point(600,200),"Close")
    closeText.setSize(25)
    closeText.draw(win)
    
    atText = Text(Point(600,700),"Attributes:")
    atText.setSize(33)
    atText.draw(win)
    
    atts = Text(Point(600,500),"Hair Color\nEye Color\nSkin Color\nFace Structure\nHair Length\nEyebrow Thickness\nGlasses\nFacial Hair\nTeeth in image")
    atts.setSize(28)
    atts.draw(win)
    
    t = True
    while t == True:
        #(IMS) 
        click = win.getMouse()
        if checkClick(click,Point(510,170),Point(690,230)) == "clicked":
            closeButton.undraw()
            closeText.undraw()
            atts.undraw()
            atText.undraw()
            cover.undraw()
            questionBox.draw(win)
            t = False
            
                        
#function to clear entire window    
def clear(win):
    for i in win.items[:]:
        i.undraw()
    win.update()        
#Function that draws directions on how to play the game prior to the start of the game  
def htpScreen(win):
    title = Text(Point(600,720),"How to Play:")
    title.setSize(36)
    title.draw(win)
    
    inst1 = Text(Point(600,500),"To play this game, you ask a series of questions using the entry box in order to try to guess which of the characters is the correct one.\n\n In order to guess a character, you must click the image of that character.\n\n Each question you ask adds one point to your total guesses.\n\n Each guess you make adds three points to your total guesses unless you are correct.\n\nThe objective is to guess the correct person in the lowest number of guesses possible. \n\n\n\nGood Luck!")
    inst1.setSize(20)
    inst1.draw(win)
    
    HomeButton = Rectangle(Point(530,260),Point(670,300))
    HomeButton.setFill("yellow")
    HomeButton.draw(win)
    
    HomeText = Text(Point(600,280),"Home")
    HomeText.setSize(24)
    HomeText.draw(win)
    
    while True:
        #(IMS) 
        click = win.getMouse()
        if checkClick(click,Point(520,250),Point(680,310)) == "clicked":
            clear(win)
            main(win)
            
#Function that creates a button on the game screen for attributes  
def drawAttributes(win):
    button = Rectangle(Point(145,120),Point(250,160))
    button.setFill("green")
    button.draw(win)
    
    txt = Text(Point(197.5,140),"Attributes")
    txt.setSize(14)
    txt.draw(win)
    
#Function to close window
def close(win):
    win.close()
#Function that creates a button on the game screen to quit the game   
def quitButton(win):
    quitB = Rectangle(Point(145,170),Point(250,210))
    quitB.setFill("red")
    quitB.draw(win)
    
    quitText = Text(Point(197.7,190),"Quit")
    quitText.setSize(14)
    quitText.draw(win)
    
#Function that draws empty text for messages on screen, calls another function to choose a character, calls another function to draw the game screen adn entry box, and calls functions to draw buttons
#Function also waits for click and calls another function to check click and test user's input against classes and updates screen
#When game ends, window is cleared and username request comes up and updated high scores
def main2(win):
    error = Text(Point(550,150),"")
    error.setSize(16)
    error.setTextColor("red")
    error.draw(win)
    
    guesses,guessTotal = createGuess(win)
    charList,imageList = create()
    char = chooseCard(charList)
    imageDraw(win,imageList)
    questionBox = questionArea(win)
    
    text = Text(Point(1000,240),"")
    text.draw(win)
    rect = Rectangle(Point(900,50),Point(1100,260))
    rect.setWidth(5)
    rect.setOutline(color_rgb(128, 0, 0))
    rect.draw(win)
    
    drawAttributes(win)
    quitButton(win)

    test = False
    while test == False:
        #(IMS) 
        click = win.getMouse()
        guesses,guessTotal = clickFunction(win,click,questionBox,char,charList,imageList,guesses,guessTotal,error)
        userGuess,guesses,guessTotal = checkImageGuess(win,click,charList,char,text,guesses,guessTotal)
        
        if userGuess != "":
            test = testCorrect(userGuess,char,text)
            
        if checkClick(click,Point(145,120),Point(250,160)) == "clicked":
            questionBox.undraw()
            attributes(win,questionBox)
            
        if checkClick(click,Point(145,170),Point(250,210)) == "clicked":
            close(win)
     
    guessTotal = updateGuess(guesses,guessTotal)
    clear(win)
    name = enterUser(win)
    clear(win)
    updateScores(win,name,guesses)
    
#Function initializes guess count and sets text up that will tell the user their score.
def createGuess(win):
    guesses = 0
    guessTotal = Text(Point(200,100),("Guesses:",guesses))
    guessTotal.setSize(22)
    guessTotal.draw(win)
    return guesses,guessTotal

#Function updates guess total by one for each question asked
def guessCount(guesses,guessTotal):
    guesses = guesses + 1
    guessTotal = updateGuess(guesses,guessTotal)
    return guesses,guessTotal

#Function that adds 3 to guess total each time the user presses an image
def imageGuess(guesses,guessTotal):
    guesses = guesses + 3
    guessTotal = updateGuess(guesses,guessTotal)
    return guesses,guessTotal

#Function that takes in new guess count and sets the text to udpated guess count
def updateGuess(guesses,guessTotal):
    guessTotal.setText(("Guesses:",guesses))
    return guessTotal
    
#Function that takes undraw list and undraws the images that are in that list
def undrawImages(undrawList,imageList):
    for img in undrawList:
        imageList[img-1].undraw()
    
#Function that draws all of the images in the list
def imageDraw(win,imageList):
    for img in imageList:
        img.draw(win)

#Function that checks entry box for specific key terms and runs specific functions based on the keywords
def clickFunction(win,click,questionBox,char,charList,imageList,guesses,guessTotal,error):
    undrawList = ""
    if checkClick(click,Point(620,89),Point(666,113)) == "clicked":
        #(IEB) 
        questionBox = questionBox.getText()
        questionBox = questionBox.lower()
        
        if "brow" not in questionBox and "eye" in questionBox or"eyes" in questionBox:
            undrawList = testEyes(questionBox,char,charList,error)
            
        elif "skin" in questionBox:
            undrawList = testSkinColor(questionBox,char,charList,error)
            
        elif "face" in questionBox or "sharp" in questionBox or "round" in questionBox:
            undrawList = testFaceStruc(questionBox,char,charList,error)
            
        elif "long" in questionBox or "short" in questionBox:
            undrawList = testHairLength(questionBox,char,charList,error)
            
        elif "thick eyebrows" in questionBox or "thin eyebrows" in questionBox:
            undrawList = testEyebrows(questionBox,char,charList,error)
            
        elif "glasses" in questionBox:
            undrawList = testGlasses(questionBox,char,charList,error)
            
        elif "teeth" in questionBox:
            undrawList = testTeeth(questionBox,char,charList,error)
            
        elif "facial hair" in questionBox:
            undrawList = testFacialHair(questionBox,char,charList,error)
            
        elif "brown hair" in questionBox or "blonde" in questionBox or "blond" in questionBox or "gray" in questionBox or "grey" in questionBox or "hair" in questionBox:
            undrawList = testHair(questionBox,char,charList,error)
            
        else:
            error.setText("I do not understand the input.\nCheck the attributes screen for hints!")
            
        if undrawList != "":
            undrawImages(undrawList,imageList)
            
        guesses,guessTotal = guessCount(guesses,guessTotal)
    return guesses,guessTotal

#Function that sets the guessImg equal to the image of the character guessed by the user
def makeGuessImg(userGuess,charList):
    
    if userGuess == charList[0]:
        guessImg = Image(Point(1000,140),"gwboy1.png")
        
    elif userGuess == charList[1]:
        guessImg = Image(Point(1000,140),"gwboy2.png")
        
    elif userGuess == charList[2]:
        guessImg = Image(Point(1000,140),"gwboy3.png")
        
    elif userGuess == charList[3]:
        guessImg = Image(Point(1000,140),"gwboy4.png")
        
    elif userGuess == charList[4]:
        guessImg = Image(Point(1000,140),"gwboy5.png")
        
    elif userGuess == charList[5]:
        guessImg = Image(Point(1000,140),"gwboy6.png")
        
    elif userGuess == charList[6]:
        guessImg = Image(Point(1000,140),"gwgirl1.png")
        
    elif userGuess == charList[7]:
        guessImg = Image(Point(1000,140),"gwgirl2.png")
        
    elif userGuess == charList[8]:
        guessImg = Image(Point(1000,140),"gwgirl3.png")
        
    elif userGuess == charList[9]:
        guessImg = Image(Point(1000,140),"gwgirl4.png")
        
    elif userGuess == charList[10]:
        guessImg = Image(Point(1000,140),"gwgirl5.png")
        
    elif userGuess == charList[11]:
        guessImg = Image(Point(1000,140),"gwgirl6.png")
        
    elif userGuess == charList[12]:
        guessImg = Image(Point(1000,140),"gwmixed1.png")
        
    elif userGuess == charList[13]:
        guessImg = Image(Point(1000,140),"gwmixed2.png")
        
    elif userGuess == charList[14]:
        guessImg = Image(Point(1000,140),"gwmixed3.png")
        
    elif userGuess == charList[15]:
        guessImg = Image(Point(1000,140),"gwmixed4.png")
        
    elif userGuess == charList[16]:
        guessImg = Image(Point(1000,140),"gwmixed5.png")
        
    elif userGuess == charList[17]:
        guessImg = Image(Point(1000,140),"gwmixed6.png")
    else:
       guessImg = Image(Point(1000,140),"blank.png") 
    return guessImg
        
#Function that tests where the user clicked and sets userGuess equal to charList index      
def checkImageGuess(win,click,charList,char,text,guesses,guessTotal):
    userGuess = ""
    guessImg = Image(Point(1000,140),"blank.png")
    if checkClick(click,Point(30,620),Point(204,799)) == "clicked":
        userGuess = charList[0]
        guesses,guessTotal=imageGuess(guesses,guessTotal)
        
    elif checkClick(click,Point(226,620),Point(398,799)) == "clicked":
        userGuess = charList[1]
        guesses,guessTotal=imageGuess(guesses,guessTotal)
        
    elif checkClick(click,Point(422,620),Point(592,799)) == "clicked":
        userGuess = charList[2]
        guesses,guessTotal=imageGuess(guesses,guessTotal)
        
    elif checkClick(click,Point(618,620),Point(786,799)) == "clicked":
        userGuess = charList[3]
        guesses,guessTotal=imageGuess(guesses,guessTotal)
        
    elif checkClick(click,Point(814,620),Point(980,799)) == "clicked":
        userGuess = charList[4]
        guesses,guessTotal=imageGuess(guesses,guessTotal)
        
    elif checkClick(click,Point(1010,599),Point(1174,799)) == "clicked":
        userGuess = charList[5]
        guesses,guessTotal=imageGuess(guesses,guessTotal)
        
    elif checkClick(click,Point(30,446),Point(204,613)) == "clicked":
        userGuess = charList[6]
        guesses,guessTotal=imageGuess(guesses,guessTotal)
        
    elif checkClick(click,Point(226,446),Point(398,613)) == "clicked":
        userGuess = charList[7]
        guesses,guessTotal=imageGuess(guesses,guessTotal)
    
    elif checkClick(click,Point(422,446),Point(592,613)) == "clicked":
        userGuess = charList[8]
        guesses,guessTotal=imageGuess(guesses,guessTotal)
        
    elif checkClick(click,Point(618,446),Point(786,613)) == "clicked":
        userGuess = charList[9]
        guesses,guessTotal=imageGuess(guesses,guessTotal)
        
    elif checkClick(click,Point(814,446),Point(971,613)) == "clicked":
        userGuess = charList[10]
        guesses,guessTotal=imageGuess(guesses,guessTotal)
        
    elif checkClick(click,Point(1010,446),Point(1174,613)) == "clicked":
        userGuess = charList[11]
        guesses,guessTotal=imageGuess(guesses,guessTotal)
        
    elif checkClick(click,Point(30,266),Point(204,432)) == "clicked":
        userGuess = charList[12]
        guesses,guessTotal=imageGuess(guesses,guessTotal)
        
    elif checkClick(click,Point(226,266),Point(398,432)) == "clicked":
        userGuess = charList[13]
        guesses,guessTotal=imageGuess(guesses,guessTotal)
        
    elif checkClick(click,Point(422,266),Point(592,432)) == "clicked":
        userGuess = charList[14]
        guesses,guessTotal=imageGuess(guesses,guessTotal)
        
    elif checkClick(click,Point(618,266),Point(786,432)) == "clicked":
        userGuess = charList[15]
        guesses,guessTotal=imageGuess(guesses,guessTotal)
        
    elif checkClick(click,Point(814,266),Point(971,432)) == "clicked":
        userGuess = charList[16]
        guesses,guessTotal=imageGuess(guesses,guessTotal)

    elif checkClick(click,Point(1010,266),Point(1174,432)) == "clicked":
        userGuess = charList[17]
        guesses,guessTotal=imageGuess(guesses,guessTotal)
        
    guessImg = makeGuessImg(userGuess,charList)
       
        

    guessImg.draw(win)
    return userGuess,guesses,guessTotal

        

#Funtion that generates a random number and sets it equal to the class of that index       
def chooseCard(charList):
    #(RND)
    card = randrange(0,18)
    userImage = charList[card]
    return userImage

#Function that tests if the user's guess for image is equal to the correct character
def testCorrect(userGuess,char,text):
    test = True
    
    if userGuess.getHairColor() != char.getHairColor():
        test = False
        
    if userGuess.getEyeColor() != char.getEyeColor():
        test = False
        
    if userGuess.getSkinColor() != char.getSkinColor():
        test = False
        
    if userGuess.getFaceStruc() != char.getFaceStruc():
        test = False
        
    if userGuess.getEyebrow() != char.getEyebrow():
        test = False
        
    if userGuess.getHairLength() != char.getHairLength():
        test = False
        
    if userGuess.getGlasses() != char.getGlasses():
        test = False
        
    if userGuess.getTeeth() != char.getTeeth():
        test = False
        
    if userGuess.getFacialHair() != char.getFacialHair():
        test = False
        
        
    if test == True:
        text.setTextColor("green")
        text.setSize(20)
        text.setText("Correct")
        
    if test == False :
        text.setTextColor("red")
        text.setSize(20)
        text.setText("Incorrect")
        
    return test


#Function that tests if the correct character has specific hair color
def testHair(questionBox,char,charList,error):
    undrawList = []
    i= 1
    
    if questionBox == "brown hair" or questionBox == "black hair":
        if char.getHairColor() == "brown":
            for c in charList:
                if c.getHairColor() !="brown":
                    undrawList.append(i)
                i += 1
                
        if char.getHairColor() != "brown":
            for c in charList:
                if c.getHairColor() =="brown":
                    undrawList.append(i)
                i+= 1
                
        error.setText("")
        
    elif questionBox == "blonde hair" or questionBox == "blond hair":
        if char.getHairColor() == "blonde":
            for c in charList:
                if c.getHairColor() !="blonde":
                    undrawList.append(i)
                i += 1
                
        if char.getHairColor() != "blonde":
            for c in charList:
                if c.getHairColor() == "blonde":
                    undrawList.append(i)
                i+= 1
                
        error.setText("")
        
    elif questionBox == "gray hair" or questionBox == "grey hair":
        if char.getHairColor() == "gray":
            for c in charList:
                if c.getHairColor() !="gray":
                    undrawList.append(i)
                i += 1
                
        if char.getHairColor() != "gray":
            for c in charList:
                if c.getHairColor() == "gray":
                    undrawList.append(i)
                i+= 1
                
        error.setText("")
        
    else:
        error.setText("I do not recognize hair color, try 'blonde hair', 'black hair', 'brown hair', or 'gray hair'")
    
    return undrawList

#Function that tests if the correct character has specific eye color            
def testEyes(questionBox,char,charList,error):
    test = False
    undrawList = []
    i= 1
    
    if questionBox == "brown eyes":
        if char.getEyeColor() == "brown":
            test = True
            
        if test == True:
            for c in charList:
                if c.getEyeColor() !="brown":
                    undrawList.append(i)
                i += 1
                
        if test == False:
            for c in charList:
                if c.getEyeColor() =="brown":
                    undrawList.append(i)
                i+= 1
                
        error.setText("")
        
    elif questionBox == "blue eyes":
        if char.getEyeColor() == "blue":
            test = True
            
        if test == True:
            for c in charList:
                if c.getEyeColor() !="blue":
                    undrawList.append(i)
                i += 1
                
        error.setText("")
        
        if test == False:
            for c in charList:
                if c.getEyeColor() =="blue":
                    undrawList.append(i)
                i+= 1
                
        error.setText("")

    else:
        error.setText("I do not recognize eye color, try 'brown eyes' or 'blue eyes'")
    return undrawList
#Function that tests if the correct character has specific skin color
def testSkinColor(questionBox,char,charList,error):
    test = False
    undrawList = []
    i= 1
    
    if questionBox == "light skin":
        if char.getSkinColor() == "light":
            test = True
            
        if test == True:
            for c in charList:
                if c.getSkinColor() !="light":
                    undrawList.append(i)
                i += 1
                
        if test == False:
            for c in charList:
                if c.getSkinColor() =="light":
                    undrawList.append(i)
                i+= 1
                
        error.setText("")
        
    elif questionBox == "tan skin":
        if char.getSkinColor() == "tan":
            test = True
            
        if test == True:
            for c in charList:
                if c.getSkinColor() !="tan":
                    undrawList.append(i)
                i += 1
                
        if test == False:
            for c in charList:
                if c.getSkinColor() =="tan":
                    undrawList.append(i)
                i+= 1
                
        error.setText("")
        
    elif questionBox == "dark skin":
        if char.getSkinColor() == "dark":
            test = True
            
        if test == True:
            for c in charList:
                if c.getSkinColor() !="dark":
                    undrawList.append(i)
                i += 1
                
        if test == False:
            for c in charList:
                if c.getSkinColor() =="dark":
                    undrawList.append(i)
                i+= 1
                
        error.setText("")
        
    else:
        error.setText("do not recognize skin color, try 'light skin', 'tan skin', or 'dark skin'.")
    
    return undrawList
#Function that tests if the correct character has specific face structure
def testFaceStruc(questionBox,char,charList,error):
    test = False
    undrawList = []
    i= 1
    if "sharp" in questionBox:
        if char.getFaceStruc() == "sharp":
            test = True
            
        if test == True:
            for c in charList:
                if c.getFaceStruc() !="sharp":
                    undrawList.append(i)
                i += 1
                
        if test == False:
            for c in charList:
                if c.getFaceStruc() =="sharp":
                    undrawList.append(i)
                i+= 1
                
        error.setText("")
        
    elif "round" in questionBox:
        if char.getFaceStruc() == "round":
            test = True
            
        if test == True:
            for c in charList:
                if c.getFaceStruc() !="round":
                    undrawList.append(i)
                i += 1
                
        if test == False:
            for c in charList:
                if c.getFaceStruc() =="round":
                    undrawList.append(i)
                i+= 1
                
        error.setText("")
        
    else:
        error.setText("do not recognize face structure, try 'a sharp face' or 'a round face'")
    
    return undrawList

#Function that tests if the correct character has specific hair length
def testHairLength(questionBox,char,charList,error):
    test = False
    undrawList = []
    i= 1
    if questionBox == "long hair":
        if char.getHairLength() == "long":
            test = True
            
        if test == True:
            for c in charList:
                if c.getHairLength() !="long":
                    undrawList.append(i)
                i += 1
                
        if test == False:
            for c in charList:
                if c.getHairLength() =="long":
                    undrawList.append(i)
                i+= 1
                
        error.setText("")
        
    elif questionBox == "short hair":
        if char.getHairLength() == "short":
            test = True
            
        if test == True:
            for c in charList:
                if c.getHairLength() !="short":
                    undrawList.append(i)
                i += 1
                
        if test == False:
            for c in charList:
                if c.getHairLength() =="short":
                    undrawList.append(i)
                i+= 1
                
        error.setText("")
        
    else:
        error.setText("I do not recognize the question, try 'long hair' or 'short hair'")
    
    return undrawList



#Function that tests if the correct character has specific eyebrow thickness
def testEyebrows(questionBox,char,charList,error):
    test = False
    undrawList = []
    i= 1
    
    if questionBox == "thick eyebrows":
        if char.getEyebrow() == True:
            test = True
            
        if test == True:
            for c in charList:
                if c.getEyebrow() !=True:
                    undrawList.append(i)
                i += 1
                
        if test == False:
            for c in charList:
                if c.getEyebrow() ==True:
                    undrawList.append(i)
                i+= 1
                
        error.setText("")
        
    elif questionBox == "thin eyebrows":
        if char.getEyebrow() == False:
            test = True
            
        if test == True:
            for c in charList:
                if c.getEyebrow() != False:
                    undrawList.append(i)
                i += 1
                
        if test == False:
            for c in charList:
                if c.getEyebrow() ==False :
                    undrawList.append(i)
                i+= 1
                
        error.setText("")
        
    else:
        error.setText("I do not recognize eyebrow thickness, try 'thin eyebrows' or 'thick eyebrows'")
    
    return undrawList
#Function that tests if the correct character has glasses or no glasses  
def testGlasses(questionBox,char,charList,error):
    test = False
    undrawList = []
    i= 1
    
    if questionBox == "glasses":
        if char.getGlasses() == True:
            test = True
            
        if test == True:
            for c in charList:
                if c.getGlasses() !=True:
                    undrawList.append(i)
                i += 1
                
        if test == False:
            for c in charList:
                if c.getGlasses() ==True:
                    undrawList.append(i)
                i+= 1
                
        error.setText("")
        
    elif questionBox == "no glasses":
        if char.getGlasses() == False:
            test = True
            
        if test == True:
            for c in charList:
                if c.getGlasses() != False:
                    undrawList.append(i)
                i += 1
                
        if test == False:
            for c in charList:
                if c.getGlasses() ==False :
                    undrawList.append(i)
                i+= 1
                
        error.setText("")
        
    else:
        error.setText("I do not recognize the question, try 'glasses' or 'no glasses'")
    
    return undrawList
#Function that tests if the correct character has teeth or no
def testTeeth(questionBox,char,charList,error):
    test = False
    undrawList = []
    i= 1
    if questionBox == "smile with teeth" or questionBox == "teeth":
        if char.getTeeth() == True:
            test = True
            
        if test == True:
            for c in charList:
                if c.getTeeth() !=True:
                    undrawList.append(i)
                i += 1
                
        error.setText("")
                
        if test == False:
            for c in charList:
                if c.getTeeth() ==True:
                    undrawList.append(i)
                i+= 1
                
        error.setText("")
                
    elif questionBox == "smile without teeth" or questionBox == "no teeth":
        if char.getTeeth() == False:
            test = True
            
        if test == True:
            for c in charList:
                if c.getTeeth() != False:
                    undrawList.append(i)
                i += 1
                
        error.setText("")
                
        if test == False:
            for c in charList:
                if c.getTeeth() ==False :
                    undrawList.append(i)
                i+= 1

        error.setText("")
                
    else:
        error.setText("I do not recognize the question, try 'teeth' or 'no teeth'")
    
    return undrawList


#Function that tests if the correct character has facial hair
def testFacialHair(questionBox,char,charList,error):
    test = False
    undrawList = []
    i= 1
    
    if questionBox == "facial hair":
        if char.getFacialHair() == True:
            test = True
            
        if test == True:
            for c in charList:
                if c.getFacialHair() !=True:
                    undrawList.append(i)
                i += 1
                
        if test == False:
            for c in charList:
                if c.getFacialHair() ==True:
                    undrawList.append(i)
                i+= 1
                
        error.setText("")
        
    elif questionBox == "no facial hair":
        if char.getFacialHair() == False:
            test = True
            
        if test == True:
            for c in charList:
                if c.getFacialHair() != False:
                    undrawList.append(i)
                i += 1
                
        if test == False:
            for c in charList:
                if c.getFacialHair() ==False :
                    undrawList.append(i)
                i+= 1
                
        error.setText("")
        
    else:
        error.setText("I do not recognize the question, try 'facial hair' or 'no facial hair'")
    
    return undrawList



#Function that checks if user clicked within specific range (rectangle shape)
def checkClick(clickPoint,leftL,rightU):
    if (clickPoint.x > leftL.x) and (clickPoint.x < rightU.x) and (clickPoint.y > leftL.y) and (clickPoint.y < rightU.y):
        return "clicked"
    
    else:
        return "not"



#Function that creates question area on game screen   
def questionArea(win):
    #entry box with questions
    #(OTXT)
    question = Text(Point(459,100),"Do they have")
    question.setSize(22)
    question.draw(win)

    #questionbox
    questionBox = Entry(Point(570,100),10)
    questionBox.setTextColor("white")
    questionBox.draw(win)

    #button for guesses
    askButton = Rectangle(Point(620,89),Point(666,113))
    askButton.setFill("white")
    askButton.draw(win)
    
    textButton = Text(Point(643,101),"Ask!")
    textButton.draw(win)
    return questionBox



#Function that creates images and classes for each character
def create():
    #(CLOD)
    #creating images diff=180
    image1 = Image(Point(120,710), "gwboy1.png")
    image1Character = Character("blonde","light","round","blue","long",True,False,False,False)
    
    image2 = Image(Point(310,710), "gwboy2.png")
    image2Character = Character("brown","tan","sharp","brown","short",True,True,True,True)

    image3 = Image(Point(500,710), "gwboy3.png")
    image3Character = Character("brown","dark","sharp","brown","long",True,False,False,True)

    image4 = Image(Point(690,710), "gwboy4.png")
    image4Character = Character("gray","tan","round","brown","short",False,True,True,False)

    image5 = Image(Point(880,710), "gwboy5.png")
    image5Character = Character("gray","light","round","blue","short",False,True,False,False)

    image6 = Image(Point(1070,710), "gwboy6.png")
    image6Character = Character("blonde","dark","sharp","brown","short",False,False,True,True)

    image7 = Image(Point(120,530), "gwgirl1.png")
    image7Character = Character("brown","dark","sharp","brown","long",False,True,True,False)

    image8 = Image(Point(310,530), "gwgirl2.png")
    image8Character = Character("gray","tan","sharp","brown","long",True,False,False,False)

    image9 = Image(Point(500,530), "gwgirl3.png")
    image9Character = Character("blonde","light","sharp","blue","long",True,True,True,False)

    image10 = Image(Point(690,530), "gwgirl4.png")
    image10Character = Character("gray","tan","round","blue","short",False,False,True,False)

    image11 = Image(Point(880,530), "gwgirl5.png")
    image11Character = Character("blonde","light","round","blue","long",False,True,False,False)

    image12 = Image(Point(1070,530), "gwgirl6.png")
    image12Character = Character("brown","dark","round","brown","short",False,False,False,False)

    image13 = Image(Point(120,350), "gwmixed1.png")
    image13Character = Character("brown","light","sharp","brown","long",True,False,True,False)

    image14 = Image(Point(310,350), "gwmixed2.png")
    image14Character = Character("brown","dark","round","blue","short",False,True,True,False)

    image15 = Image(Point(500,350), "gwmixed3.png")
    image15Character = Character("brown","dark","round","blue","short",False,False,False,False)

    image16 = Image(Point(690,350), "gwmixed4.png")
    image16Character = Character("gray","light","round","brown","short",True,False,False,True)

    image17 = Image(Point(880,350), "gwmixed5.png")
    image17Character = Character("blonde","light","round","blue","short",False,True,True,False)

    image18 = Image(Point(1070,350), "gwmixed6.png")
    image18Character = Character("brown","tan","sharp","brown","short",True,False,False,False)

    #(LOOD)
    charList = [image1Character,image2Character,image3Character,image4Character,image5Character,image6Character,image7Character,image8Character,image9Character,image10Character,image11Character,image12Character,image13Character,image14Character,image15Character,image16Character,image17Character,image18Character]
    imageList= [image1,image2,image3,image4,image5,image6,image7,image8,image9,image10,image11,image12,image13,image14,image15,image16,image17,image18]
    
    return charList,imageList






#Class that has attributes for each character with display method and get method for each attribute to use in game
#(CLOD)
class Character:
    def __init__(self,hairColor,skinColor,faceStruc,eyeColor,hairLength,thickEyebrows=False,glasses=False,teeth=False,facialHair=False):
        self.hairColor = hairColor
        self.glasses = glasses
        self.skinColor = skinColor
        self.teeth = teeth
        self.faceStruc = faceStruc
        self.eyeColor = eyeColor
        self.hairLength = hairLength
        self.thickEyebrows = thickEyebrows
        self.facialHair = facialHair
        
    def display(self):
        print("{0:<10}{1:<10}{2:<10}{3:<10}{4:<9}{5}    {6}    {7}   {8}".format(self.hairColor,self.skinColor,self.faceStruc,self.eyeColor,self.hairLength,self.glasses,self.teeth,self.thickEyebrows,self.facialHair))

    def getHairColor(self):
        return self.hairColor

    def getSkinColor(self):
        return self.skinColor

    def getFaceStruc(self):
        return self.faceStruc

    def getEyeColor(self):
        return self.eyeColor

    def getHairLength(self):
        return self.hairLength

    def getEyebrow(self):
        return self.thickEyebrows

    def getGlasses(self):
        return self.glasses

    def getTeeth(self):
        return self.teeth

    def getFacialHair(self):
        return self.facialHair
#(FNC)    
createScreen()





