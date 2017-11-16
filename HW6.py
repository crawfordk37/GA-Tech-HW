##Crawford Kennedy, 17ckennedy@woodward.edu, CS1301
##I worked on the homework assignment alone, using only this semester's course materials.
def getDict(inputFile):
    inFile = open(inputFile, "rt")
    data = inFile.readlines()
    inFile.close()
    finalDict = {}
    for line in data:
        foundFirst = 0
        foundLast = 0
        foundClass = 0
        foundGrade = 0
        foundHours = 0
        firstName = ''
        lastName = ''
        name = ''
        className = ''
        grade = ''
        hours = ''
        classList = []
        generatedList = 0
        for character in line:
            if foundLast == 0:
                if character == ',':
                    foundLast = 1;
                elif character != ' ':
                    lastName += character
            elif foundFirst == 0:
                if character == ':':
                    foundFirst = 1;
                elif character != ' ':
                    firstName += character
            elif character != ' ' and character != '[' and character != '\\':
                if generatedList == 1:
                    foundClass = 0
                    foundGrade = 0
                    foundHours = 0
                    className = ''
                    grade = ''
                    hours = ''
                    generatedList = 0
                if foundClass == 0:
                    if character == ',':
                        foundClass = 1
                    else:
                        className += character
                elif foundGrade == 0:
                    if character == ',':
                        foundGrade = 1
                    else:
                        grade += character
                elif foundHours == 0:
                    if character == ']':
                        foundHours = 1
                    else:
                        hours += character
                else:
                    formattedClass = []
                    formattedClass.append(className)
                    formattedClass.append(int(grade))
                    formattedClass.append(int(hours))
                    classList.append(formattedClass)
                    generatedList = 1
                    name = firstName + ' ' + lastName
                    finalDict[name] = classList
    return finalDict


def calcGPA(student, aDict):
    if aDict == []:
        return 0.0
    try:
        classes = aDict[student]
    except KeyError:
        return 0.0
    if classes == []:
        return 0.0
    totalCredits = 0.0
    totalCreditHours = 0
    for item in classes:
        if item[1] >= 90:
            grade = 4
        elif item[1] >= 80:
            grade = 3
        elif item[1] >= 70:
            grade = 2
        elif item[1] >= 60:
            grade = 1
        else:
            grade = 0
        totalCredits += grade * item[2]
        totalCreditHours += item[2]
    return round(totalCredits/totalCreditHours, 1)


def newFile(classList, aDict, outputFile):
    outFile = open(outputFile, "wt")
    for item in classList:
        found = 0
        outFile.write(item)
        outFile.write(':')
        outFile.write(' ')
        for student in aDict:
            l = aDict[student]
            for className in l:
                if className[0] == item and found == 0:
                    outFile.write(student)
                elif className[0] == item:
                    outFile.write(',')
                    outFile.write(' ')
                    outFile.write(student)
        outFile.write('\n')
    outFile.close()
