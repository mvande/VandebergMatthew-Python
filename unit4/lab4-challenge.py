#Matthew Vandeberg
#Python
#Period 2

def main():
    bonusOne()
    bonusTwo()

def bonusOne():
    for i in range(7):
        line = ''
        if(i == 0 or i == 6):
            for j in range(7):
                line += '*'
        else:
            for k in range(7):
                if(k == 0 or k == 6):
                    line += '*'
                else:
                    line += '-'
        print(line)

def bonusTwo():
    string = ''
    for i in range(1, 8): #Loops from 1 to 7. This loop keeps track of the number to be printed in each line.
        string += str(i)
        for j in range(i):
            print(string)
        

main()