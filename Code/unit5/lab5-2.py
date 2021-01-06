#Matthew Vandeberg
#Python
#Period 2

from Code.unit5.lab5Classes import * #Import everything from lab5Classes file (remove 'Code' from import statement when grading)

def main():

    myDog = dog('golden', 'doge', 'medium hair') #Create dog called myDog
    print(myDog.activity()) #Print what myDog does

    myCat = cat('grey', 'grumpy', 'short hair') #Create dog called myCat
    print(myCat.activity()) #Print what myCat does

main()