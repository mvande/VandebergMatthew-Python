#Matthew Vandeberg
#Python
#Period 2

#The bane of every programmer; documentation

def main(): #Calls goTeam and theBest functions two times each with blank lines in-between
    goTeam()
    print()
    theBest()
    print()
    theBest()
    print()
    goTeam()

def goTeam(): #Function to print out stuff for goTeam function
    print("Go, team, go!")
    print("You can do it.")

def theBest(): #Calls goTeam twice and use two print statements to print the stuff out for theBest function
    goTeam()
    print("You are the best,")
    print("In the West.")
    goTeam()

main()