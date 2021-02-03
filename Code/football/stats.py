#Matthew Vandeberg
#Python
#Period 2

from Code.football.footballClasses import * #Import football classes

def main():
    #Create quarterBack object and print all required info
    qb1 = quarterBack('seahawks', 'wilson', '3', 12, 250, 1500)
    print(qb1.playerInfo())
    print(qb1.activity())
    print(qb1.pointsGame())
    print(qb1.yardsGame())

    print()

    #Create receiver object and print all required info
    rc1 = receiver('seahawks', 'baldwin', '89', 16, 300, 2000)
    print(rc1.playerInfo())
    print(rc1.activity())
    print(rc1.pointsGame())
    print(rc1.receivingYardsGame())

    print()

    #Create runningBack object and print all required info
    rb1 = runningBack('seahawks', 'lynch', '24', 15, 150, 2200)
    print(rb1.playerInfo())
    print(rb1.activity())
    print(rb1.pointsGame())
    print(rb1.runningYardsGame())

main()