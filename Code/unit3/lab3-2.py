#Matthew Vandeberg
#Python
#Period 2

def main(): #Lines 8-9 are for lab 3-2A and lines 14-15 are for lab 3-2B.
    #Passes the number of boxes to draw in the console, the character to use for the sides,
    #and the character to use for the top and bottom.
    drawBoxes(3, "#", "@") 

    print() #Just to space out the two labs

    #Create a list of names and then passes that list and an index number to the printName function.
    names = ["Matthew", "Jaxson", "Dan", "Joe", "Laura"]
    printName(names, 0)

#Takes in three parameters and uses an if/elif/else statement to call the
#drawBox function a certain number of times based on the numBoxes parameter.
#Also prints title according to number of boxes to print
#Each time drawBoxes calls drawBox, it passes sideChar and topBotChar to drawBox.
def drawBoxes(numBoxes, sideChar, topBotChar):
    if numBoxes == 3:
        print("draw three boxes \n")
        drawBox(sideChar, topBotChar)
        drawBox(sideChar, topBotChar)
        drawBox(sideChar, topBotChar)
    elif numBoxes == 2:
        print("draw two boxes \n")
        drawBox(sideChar, topBotChar)
        drawBox(sideChar, topBotChar)
    elif numBoxes == 1:
        print("draw one box \n")
        drawBox(sideChar, topBotChar)
    else:
        print("Only able to print 1 to 3 boxes. Please pass a 1, 2, or 3 to the drawBoxes function in main.")

#Uses a blank print statement to space out the boxes then calls the drawTopBot and drawSide functions to draw a box.
def drawBox(side, topBot):
    print()
    drawTopBot(topBot)
    drawSide(side)
    drawSide(side)
    drawTopBot(topBot)

#Function to draw the sides of a box using the sideSymbol parameter.
def drawSide(sideSymbol):
    print(sideSymbol + "    " + sideSymbol)

#Function to draw the top and bottom of a box using the topBotSymbol parameter.
def drawTopBot(topBotSymbol):
    print(topBotSymbol + topBotSymbol + topBotSymbol + topBotSymbol + topBotSymbol + topBotSymbol)

#printName function is for lab 3-2B
#Function that prints a name at a given index in a list
def printName(list, index):
    print("The name at index number " + str(index) + " is:")
    print(list[index])

main()