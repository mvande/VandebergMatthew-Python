#Matthew Vandeberg
#Python
#Period 2

def main():
    #Create loop from 2 to 6 that prints 2 through 6 and the product of each number and ten.
    for i in range(2, 7):
        print("index " + str(i) + " - " + str(i * 10))

    #Create list of fruits and pass it to the fruitPlural function.
    fruitList = ["banana", "apple", "orange", "grape"]
    fruitPlural(fruitList)

#Loops through the passed list and adds an "s" to each string in the list and then prints the modified list.
def fruitPlural(list):
    for i in range(0, len(list)):
        list[i] += "s"
    print(str(list))

main()