#Matthew Vandeberg
#Python
#Period 2

def main():
    #While loop continously gets an input and runs the deVowel function.
    repeat = 'y'
    while(repeat == 'y'):
        inputString = input("gib string: ")
        print(deVowel(inputString))
        repeat = input("Continue? (y/n): ") #Allows user to escape the while loop.

    #Create a list of 4 numbers and pass it to mathStuff function with a multiplier and print returned value.
    numList = [1, 2, 3, 4]
    print(mathStuff(numList, 5))

#Removes vowels from a given string.
def deVowel(word):
    noVowels = ''
    #Loops through the passed string and add everything that isn't a vowel to a string.
    for char in word:
        if char not in ['a', 'e', 'i', 'o', 'u']: #if statement to check if the given character is not a vowel.
            noVowels += char
    return noVowels #Return the string with vowels removed.

#Multiples every value of the given list by a given number.
def mathStuff(list, multi):
    newList = [] #Create a new empty list
    #Iterate through list and append multiplied number from the given list to the new list.
    for num in list:
        newList.append(num * multi)
    return str(newList) #Return the new list as a string.

main()