#Matthew Vandeberg
#Python
#Period 2

from random import randint

def main():
    play = 'y'
    gameNum = 0;
    dice = defineDice()
    while play == 'y':
        printDice(dice[rollDice() - 1])
        gameNum += 1
        play = input('continue? (y/n) ')
        drawLine()
    print('Numbers of games played: ' + str(gameNum))

def defineDice():
    setOfDice = [0] * 6

    topBot = ' ------- '
    space = '|       |'
    oneDotL = '| *     |'
    oneDotM = '|   *   |'
    oneDotR = '|     * |'
    twoDot = '| *   * |'
    
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
    
    return(setOfDice)

def rollDice():
    random = randint(1, 6)
    return(random)

def printDice(die):
    for part in die:
        print(part)

def drawLine():
    line = ''
    for i in range(10):
        line += '--'
    print(line)
        

main()