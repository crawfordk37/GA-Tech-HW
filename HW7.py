##Crawford Kennedy, 17ckennedy@woodward.edu, CS1301
##I worked on the homework assignment alone, using only this semester's course materials.
import math
def square_contents(numList, position = 0):
    numList[position] = (numList[position])**2
    if position < len(numList)-1:
        position += 1
        square_contents(numList, position)
    return numList
def factorial_dictionary(num, factorialDict = {}):
    if num != 1:
        factorialDict[num] = math.factorial(num)
        factorial_dictionary(num-1, factorialDict)
        return factorialDict
    else:
        factorialDict[num] = 1
def solve_eq(inputString, isFirst = True, string = ''):
    good = set('1234567890.')
    if isFirst:
        inputString = inputString.replace(" ", "")
        string = inputString[:]
    if set(inputString) <= good and ('/' in string or '.' in string):
        return float(inputString)
    elif set(inputString) <= good:
        return int(inputString)
    for operator in ('-','+','/','*'):
        third = inputString.partition(operator)
        if third[1] == '-':
            return solve_eq(third[0], isFirst = False, string = string)-solve_eq(third[2], isFirst = False, string = string)
        elif third[1] == '+':
            return solve_eq(third[0], isFirst = False, string = string)+solve_eq(third[2], isFirst = False, string = string)
        elif third[1] == '/':
            return solve_eq(third[0], isFirst = False, string = string)/solve_eq(third[2], isFirst = False, string = string)
        elif third[1] == '*':
            return solve_eq(third[0], isFirst = False, string = string)*solve_eq(third[2], isFirst = False, string = string)
