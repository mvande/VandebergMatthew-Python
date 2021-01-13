#Matthew Vandeberg
#Python
#Period 2

from Code.unit5.lab5Classes import *

def main():

    myGrades = grades('Matthew', 85, 90, 95, 88)
    printGrades(myGrades)
    myGrades.setEnglish(myGrades.getEnglish() + 5)
    myGrades.setMath(myGrades.getMath() + 5)
    myGrades.setPython(myGrades.getPython() + 5)
    myGrades.setHistory(myGrades.getHistory() + 5)
    printGrades(myGrades)

def printGrades(grd):
    print(grd.getName())
    print('English: ' + str(grd.getEnglish()))
    print('Math: ' + str(grd.getMath()))
    print('Python: ' + str(grd.getPython()))
    print('History: ' + str(grd.getHistory()))
    print()

main()