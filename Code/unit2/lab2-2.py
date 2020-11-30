#Matthew Vandeberg
#Python
#Period 2

def main():
    #Store user's input as a int using typecasting and an input statement
    numGrade = int(input("Input numerical Grade: "))

    #Print something based on the user input using if/elif/else statements
    if numGrade >= 90:
        print("Yahoo you got an A!")
    elif numGrade >= 80:
        print("Good you got a B!")
    elif numGrade >= 70:
        print("Okay you got a C!")
    else:
        print("You better study harder")

    #Store user's favorite color in a variable
    #Personally would've called this variable "favColor" but "userInput" works too
    userInput = input("What's your favorite color? ")

    #Print something based on user's fav color using if/elif/else statements
    if userInput == "blue": 
        print("The sky is blue")
    elif userInput == "green":
        print("The Forest is green")
    elif userInput == "red":
        print("I love red")
    elif userInput == "yellow":
        print("Yuck yellow")
    else:
        print("I am a dumb computer - I only know 4 colors")
main()