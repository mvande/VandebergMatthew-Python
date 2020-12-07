#Matthew Vandeberg
#Python
#Period 2

from random import randint #import randint function from random

def main():
    play = 'y' #While loop variable
    gameNum = 0 #Keeps track of dice rolls
    diceSet = defineDice() #Call defineDice to create a set of dice from 1 to 6

    #While loop to keep rolling dice until the user enters something other than 'y'
    while play == 'y':
        printDice(diceSet[rollDice() - 1])  #Prints the graphical version of the dice returned from rollDice
        gameNum += 1 #Adds 1 to the total of games played
        play = input('continue? (y/n) ') #Asks user if they want to continue
        drawLine() #Draws a line between each dice roll
    
    print('Numbers of games played: ' + str(gameNum)) #Prints the total number of dice rolls at the end

#Returns list of dice from 1 to 6
def defineDice():
    setOfDice = [0] * 6 #Create an empty list

    #Define the different parts of a dice
    topBot = ' ------- '
    space = '|       |'
    oneDotL = '| *     |'
    oneDotM = '|   *   |'
    oneDotR = '|     * |'
    twoDot = '| *   * |'
    
    #Loops through list of dice and assembles each die as a list at the proper index
    for i in range(6):
        if i == 0:
            setOfDice[i] = [topBot, space, oneDotM, space, topBot]
        elif i == 1:
            setOfDice[i] = [topBot, space, twoDot, space, topBot]
        elif i == 2:
            setOfDice[i] = [topBot, oneDotL, oneDotM, oneDotR, topBot]
        elif i == 3:
            setOfDice[i] = [topBot, twoDot, space, twoDot, topBot]
        elif i == 4:
            setOfDice[i] = [topBot, twoDot, oneDotM, twoDot, topBot]
        else:
            setOfDice[i] = [topBot, twoDot, twoDot, twoDot, topBot]
    
    return(setOfDice) #Return the lsit of dice

#Returns a random number between 1 and 6 to represent a dice roll
def rollDice():
    random = randint(1, 6)
    return(random)

#Loops through the list of the given die to print each part in order
def printDice(die):
    for part in die:
        print(part)

#Draws a line in the terminal
def drawLine():
    line = ''
    for i in range(10):
        line += '--'
    print(line)
        

main()