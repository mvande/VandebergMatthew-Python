#Matthew Vandeberg
#Python
#Period 2

def main():
    #Create a list of shopping lists and pass it to the two functions
    shoppingCart = [["tooth paste", "q-tips", "milk"],["milk", "candy", "apples"],["paper", "pencils", "q-tips"]]
    allInOne(shoppingCart)
    countQtips(shoppingCart)

#Combines all of the shopping lists into a single list
def allInOne(cart):
    comboList = []
    for list in cart: #Loops through the list of lists
        for item in list: #Loops through the items in each list
            comboList.append(item) #Add each item to the combo list
    print(comboList) #Print the combined list

#Prints the number of times q-tips appears in all the lists
def countQtips(lists):
    qtips = 0
    for list in lists: #Loops through the list of lists
        for item in list: #Loops through the items in each list
            if(item == 'q-tips'): #Increase the count of q-tips by one if the item is a q-tip
                qtips += 1
    print("# of q-tips = " + str(qtips)) #Print the total amount of q-tips in all the lists

main()