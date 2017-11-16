##Crawford Kennedy, CS1301, 17ckennedy@woodward.edu
##I worked on the homework assignment alone, using only this semester's course materials
def multiplyNums(nums):
    index = 1
    for num in nums: ##runs through all of the numbers
        if index<len(nums): ##confirms we won't be going out of the range
            nums[index-1] = num*nums[index] ##changes the number to be multiplied by the next number
        else: ##used to do the different thing for the last number
            nums[index-1] *= num
        index += 1
    return nums
def multiplyNums2(nums):
    nums2 = list(nums) ##same program as above but I created a second identical array to edit
    index = 1
    for num in nums2:
        if index<len(nums):
            nums2[index-1] = num*nums2[index]
        else:
            nums2[index-1] *= num
        index += 1
    return nums2
def pairExists(nums, add):
    length = len(nums)
    found = False ##presets the output so it only needs to be reset if the output is true
    for firstNum in range(length):##grabs the first number in the addition problem
        for secondNum in range(firstNum+1,length): ##looks through all of the others numbers for a number to add up with it and equal the given number
            if nums[firstNum]+nums[secondNum] == add:
                found = True ##sets the output to true if a pair is found
    return found
def listSymmetric(nums):
    length = len(nums)-1
    index = 0
    symmetric = True
    for num in nums: ##takes longer because it checks through each set twice, but its simpler. And you know what they say, "Always double check your work!" 
        if(nums[index] != nums[length-index]): ##checks if the mirrored position is equal
            symmetric = False ##sets the output to false if any mirror spot isn't equal
        index += 1 ##moves to the next set of locations
    return symmetric
def replaceStr(a, b, c):
    return a.replace(b, c) ##use replace to replace all instances of b with c in string a
def polyAlphaCipher(string, increment):
    newString = "" ##sets up the string that will be output
    change = 1 ##sets the first change
    for character in string: ##cycles through each character
        num = ord(character) ##breaks the character down into the ASCII character code
        num += change%255 ##changes the code by some amount less than or equal to 255
        newString += chr(num) ##adds the new character (found from the edited character code) to the output string
        change += increment ##increases the change by the set increment
    return newString
def polyAlphaDecipher(string, increment):
    newString = ""
    change = 1
    for character in string:
        num = ord(character)
        num -= change%255 ##same as above except this one minus is here instead of a plus. It just needs to "un-edit" the ASCII character code by taking out the increment
        newString += chr(num)
        change += increment
    return newString
