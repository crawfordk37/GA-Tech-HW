## Crawford Kennedy, CS1301, 17ckennedy@woodward.edu
## I worked on the homework assignment alone, using only this semester's course materials.

def abbreviator(inputString):
    string = 'QWERTYUIOPASDFGHJKLZXCVBNM1234567890'
    newString = ''
    for character in inputString:
        if character in string:
            newString += character
    return newString
## abbreviator is just O(n) because you only need to find a few letters and you are using for loops
def union(unsortedList1, unsortedList2):
    combinedList = []
    for number in unsortedList1:
        same = 0
        for numbers in unsortedList2:
            if number == numbers:
                same = 1
        if same == 0:
            combinedList.append(number)
    for number in unsortedList2:
        same = 0
        for numbers in combinedList:
            if number == numbers:
                same = 1
        if same == 0:
            combinedList.append(number)
    return sorted(combinedList)
## union is O(n log n) because it uses the generic sort algorithm from python which is O(n log n)
def tupleMagic(aList):
    index = 0
    for tup in aList:
        total = 0
        average = 0
        for number in tup:
            total += number
        average = total/len(tup)
        aList[index] = (average,) + tup
        index += 1
##tupleMagic is O(n) because it uses nested for loops and they just try to obtain values
def reverseMultiTable(integer):
    aList = []
    for number1 in range((-(integer)), 0):
        for number2 in range((-(integer)), 0):
            aList.append(number1*number2)
    for numbers in range(integer):
        for number in range(integer):
            addition = aList[number+(numbers*integer)]
            print(str(addition).ljust(4),end = '')
        print('\n')
##reverseMultiTable is O(n) because it just multiplies numbers with a system of for loops
def charCount(string):
    newDict = {}
    while len(string) > 0:
        count = 0
        char = string[0]
        for char2 in string:
            if char == char2:
                count += 1
        if not(char == ' '):
            newDict[char] = count
        elif char == ' ':
            print('First Space')
            newDict[None] = count
            if count > 1:
                for instance in range(1, count):
                    print('ANOTHA ONE')
        string = string.replace(char,'')
    return newDict
##charCount is also O(n) for the same reasons, it uses for loops and uses them to find a single value
def chetify(file):
    inFile = open(file, 'r')
    newFileLines = inFile.readlines()
    inFile.close()
    index = 0
    for line in newFileLines:
        line = line.replace("Young", 'Yung')
        line = line.replace("you", 'we')
        line = line.replace("yea", 'yee')
        line = line.replace("like", 'about')
        newFileLines[index] = line
        intex += 1
    outFile = open('chetify.txt', 'w')
    for line in newFileLines:
        outFile.write(line)
    outFile.close()
##chetify if O(n) because it uses for loops for simple operations
