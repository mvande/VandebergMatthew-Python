#Matthew Vandeberg
#Python
#Period 2

from Code.unit5.lab5Classes import * #Import everything from lab5Classes file (remove 'Code' from import statement when testing)

def main():

    myPet1 = pet1('black', 'username', 'long hair')
    print(myPet1.activity())

    myDog = dog('golden', 'doge', 'medium hair')
    print(myDog.activity())

    myCat = cat('grey', 'grumpy', 'short hair')
    print(myCat.activity())

main()