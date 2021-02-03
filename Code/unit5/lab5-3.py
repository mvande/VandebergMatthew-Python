#Matthew Vandeberg
#Python
#Period 2

from Code.unit5.lab5Classes import * #Import everything from lab5Classes

def main():
    myGrades = grades('Matthew', 85, 90, 95, 88) #Create grades object with a name and grades
    printGrades(myGrades) #Prints the student's name and initial grades

    #Adds five to each grade
    myGrades.setEnglish(myGrades.getEnglish() + 5)
    myGrades.setMath(myGrades.getMath() + 5)
    myGrades.setPython(myGrades.getPython() + 5)
    myGrades.setHistory(myGrades.getHistory() + 5)

    #Prints student's name and new grades
    printGrades(myGrades)

#Prints student's name and all grades
def printGrades(grd):
    print(grd.getName())
    print('English: ' + str(grd.getEnglish()))
    print('Math: ' + str(grd.getMath()))
    print('Python: ' + str(grd.getPython()))
    print('History: ' + str(grd.getHistory()))
    print()

main()