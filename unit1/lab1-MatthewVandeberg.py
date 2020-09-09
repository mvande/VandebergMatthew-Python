#Matthew Vandeberg
#Period 2 Intro to Python

def main():
    #Asks for user's first and last name using input statements
    fName = input("Please enter your first name: ")
    lName = input("Please enter your last name: ")

    #Prints user's name using print statement
    print(fName + " " + lName)

    #Prints the results of a bunch of math operations using print statements
    print(9 + 4.5)
    print(3 - 4)
    print(10 ** 2.0)
    print(4 % 2)
    print(30 / 5.0)
    print(4 * 2)

    #Asks user for two numbers and casts them as floats using input statements and type casting
    numOne = float(input("Enter a number: "))
    numTwo = float(input("Enter another number: "))

    #Prints the sum of the two numbers by casting the sum to a string and using a print statement
    print("Results: " + str(numOne + numTwo))
main()