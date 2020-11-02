#Matthew Vandeberg
#Python
#Period 2

def main():
    draw7()

    print()

    incTriangle()

#Uses nested for loops to print a 7x7 square of * characters.
def draw7():
    for i in range(7): #Loops from 0 to 6.
        for j in range(7): #Loops from 0 to 6.
            print('* ', end='') #Prints '* '. end='' changes what prints after '* ' from '\n' to ''.
        print() #Moves to a new line.
    
#Uses nested for loops to print a stack of numbers 1 to 7.
def incTriangle():
    for i in range(1, 8): #Loops from 1 to 7. This loop keeps track of the number to be printed in each line.
        for j in range(i): #Loops from 0 to i. This loop determines how many numbers are printed per line.
            print(i, end='') #Prints the value of i from the outer loop and changes the end character to ''.
        print() #Moves to a new line.

main()