#Matthew Vandeberg
#Python
#Period 2

from random import *

def main():
    numList = [4.5, 11.4, 10.7, 5.68, 1.0, 2.3] #Creates list of floats
    print(calcList(numList, "+")) #Pass list of floats and an operator to the calcList function, then print the returned value

    userIn = input("enter 1 for area and 2 for perimeter: ") #Asks for an input of 1 or 2 to calculate area or perimeter
    length = float(input("length: ")) #Asks user for length of object
    width = float(input("width: ")) #Asks user for width of object

    #If/elif/else statement passes the length & width of object to calcArea or calcPerim depending on user input and prints returned value. 
    #Also tells user if input was invalid.
    if(userIn == "1"):
        print(calcArea(length, width))
    elif(userIn == "2"):
        print(calcPerim(length, width))
    else:
        print("Error: User input invalid: " + userIn)

#Function accepts a list and a arithmetic operator.
#Then takes two objects from the list at random 
#and returns the operation indicated by the operator parameter.
def calcList(myList, mathOp):
    index1 = randint(0, len(myList) - 1)
    index2 = randint(0, len(myList) - 1)

    print("index1 = " + str(index1) + " | index2 = " + str(index2))

    if(mathOp == "+"):
        return(myList[index1] + myList[index2])
    elif(mathOp == "-"):
        return(myList[index1] - myList[index2])
    elif(mathOp == "*"):
        return(myList[index1] * myList[index2])
    elif(mathOp == "/"):
        return(myList[index1] / myList[index2])
    elif(mathOp == "%"):
        return(myList[index1] % myList[index2])
    elif(mathOp == "**"):
        return(myList[index1] ** myList[index2])
    elif(mathOp == "//"):
        return(myList[index1] // myList[index2])
    else:
        return("Invalid arithmetic operator")

def calcArea(lengthA, widthA):
    return(lengthA * widthA)

def calcPerim(lengthB, widthB):
    return(2 * (lengthB + widthB))

main()