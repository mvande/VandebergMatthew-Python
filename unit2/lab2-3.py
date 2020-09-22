#Matthew Vandeberg
#Python
#Period 2

def main():
    #Make list of 10 numbers and print it to console
    numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("List: " + str(numList))

    #Print the length of the list and the first and last numbers of the list
    print("List length: " + str(len(numList)))
    print("First num: " + str(numList[0]))
    print("Last num: " + str(numList[len(numList) - 1]))

    #Make subList that contains first 5 numbers of numList
    subList = numList[0:5]

    #Insert 3.5 at index 3 of subList and append 6 to end of subList
    subList.insert(3, 3.5)
    subList.append(6)

    #Make new list called subList1 that is a copy of subList with 7 appened at the end
    subList1 = subList + [7]

    #Make list of myClasses and remove least favorite class using remove command
    myClasses = ["Comp Sci TA", "Python", "Senior Comp", "Physics C", "Calc AB", "Ignation Formation", "American Gov", "Crafts"]
    myClasses.remove("Senior Comp")

    #Use pop command to pop first class from list and assign it to a variable
    firstClass = myClasses.pop(0)

    #Print the firstClass variable in a sentence
    print("My first class is " + firstClass)

main()