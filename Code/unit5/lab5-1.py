#Matthew Vandeberg
#Python
#Period 2

from Code.unit5.lab5Classes import * #Import everything from lab5Classes file (remove 'Code' from import statement when testing)

def main():
    myPet1 = pet('dog', 'Hanz', 'german shepard') #Create a new pet with the required info
    print(myPet1.name) #Print pet name
    print(myPet1.petType) #Print what type the pet is (caged or not)
    myPet1.whatIsIt() #Print all the info of the pet

    print()

    myPet2 = pet('cat', 'Franz', 'pixie-bob') #Create a new pet with the required info
    print(myPet2.name) #Print pet name
    print(myPet2.petType) #Print what type the pet is (caged or not)
    myPet2.whatIsIt() #Print all the info of the pet

    print()

    myCage1 = cage('snake', True) #Create a new caged pet with proper parameters
    print(myCage1.type) #Print the identity of the pet
    print(myCage1.petType) #Print what type the pet is (caged or not)
    myCage1.whatDanger() #Print whether the pet is dangerous or not

    print()

    myCage2 = cage('rat', False) #Create a new caged pet with required parameters
    print(myCage2.type) #Print the identity of the pet
    print(myCage2.petType) #Print what type the pet is (caged or not)
    myCage2.whatDanger() #Print whether the pet is dangerous or not

main()