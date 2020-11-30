#Matthew Vandeberg
#Python
#Period 2

#Obvious comments are obvious

def main(): #Prints the title and then uses the drawBox function to print boxes
    print("draw three boxes \n")
    drawBox()
    print()
    drawBox()
    print()
    drawBox()

def drawTopBot(): #Function to print the top and bottom of a box
    print("******")

def drawSides(): #Function to print the sides of a box
    print("|    |")

def drawBox(): #Uses the drawTopBot and drawSides functions to print a box
    drawTopBot()
    drawSides()
    drawSides()
    drawTopBot()

main()
