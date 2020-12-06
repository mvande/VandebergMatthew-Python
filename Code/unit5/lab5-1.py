from Code.unit5.lab5Classes import *

def main():
    myPet1 = pet('dog', 'Hanz', 'german shepard')
    print(myPet1.name)
    print(myPet1.petType)
    myPet1.whatIsIt()

    myPet2 = pet('cat', 'that one', 'feral')
    print(myPet2.name)
    print(myPet2.petType)
    myPet2.whatIsIt()

    myCage1 = cage('snake', True)
    print(myCage1.type)
    print(myCage1.petType)
    myCage1.whatDanger()

    myCage2 = cage('rat', False)
    print(myCage2.type)
    print(myCage2.petType)
    myCage2.whatDanger()

main()