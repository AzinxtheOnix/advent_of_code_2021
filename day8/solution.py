import sys
sys.path.append("../")

from fileRead import readInput

def digitElementAnalysis(elementList):
    digitComposition = ['', '', '', '', '', '', '', '', '', '']
    elementOrder = ['', '', '', '', '', '', '']
    for x in range(0, len(elementList)):                # Figure out digit composition for 1, 4, 7, and 8
        if(len(elementList[x]) == 2):
            digitComposition[1] = elementList[x]
        elif(len(elementList[x]) == 3):
            digitComposition[7] = elementList[x]
        elif(len(elementList[x]) == 4):
            digitComposition[4] = elementList[x]
        elif(len(elementList[x]) == 7):
            digitComposition[8] = elementList[x]

    for x in range(0, len(digitComposition[7])):        # Figure out element 1
        if digitComposition[7][x] in digitComposition[1]:
            pass
        else:
            elementOrder[0] = digitComposition[7][x]
    
    for x in range(0, len(elementList)):
        if(len(elementList[x]) == 6):                   # Could be digit 9
            missingElements = 0
            missingElement = ''
            for y in range(0, len(elementList[x])):
                if elementList[x][y] in digitComposition[4] or elementList[x][y] == elementOrder[0]:
                    pass
                else:
                    missingElements += 1
                    missingElement = elementList[x][y]

            if(missingElements == 1):                   # It's digit 9
                digitComposition[9] = elementList[x]
                elementOrder[6] = missingElement

    for x in range(0, len(digitComposition[8])):        # Now to figure out the missing element
        if digitComposition[8][x] in digitComposition[4] or digitComposition[8][x] == elementOrder[0] or digitComposition[8][x] == elementOrder[6]:
            pass
        else:
            elementOrder[4] = digitComposition[8][x]

    two_four = []                                       # This is ugly
    for x in range(0, len(digitComposition[4])):
        if digitComposition[4][x] not in digitComposition[1]:
            two_four.append(digitComposition[4][x])

    for x in range(0, len(elementList)):                # Note to self: I need to program stuff more consistently, the original code in this check messed something up
        if(len(elementList[x]) == 5):                   # Could be digit 3
            if digitComposition[1][0] in elementList[x] and digitComposition[1][1] in elementList[x] and elementOrder[0] in elementList[x] and elementOrder[6] in elementList[x] and ((two_four[0] in elementList[x] and two_four[1] not in elementList[x]) or ((two_four[0] not in elementList[x] and two_four[1] in elementList[x]))):
                    digitComposition[3] = elementList[x]    # It's digit 3

    for x in range(0, len(digitComposition[4])):        # Now to determine order of elements 2 and 4
        if digitComposition[4][x] not in digitComposition[3]:
            elementOrder[1] = digitComposition[4][x]
        if digitComposition[4][x] in digitComposition[3] and digitComposition[4][x] not in digitComposition[1]:
            elementOrder[3] = digitComposition[4][x]
    
    element1 = digitComposition[1][0]
    element2 = digitComposition[1][1]
    for x in range(0, len(elementList)):                # Now to figure out the order of the last two elements
        if(len(elementList[x]) == 5):                   # Could be digit 2 (man, what a long if statement)
            if elementOrder[0] in elementList[x] and element1 in elementList[x] and elementOrder[3] in elementList[x] and elementOrder[4] in elementList[x] and elementOrder[6] in elementList[x]:
                elementOrder[2] = element1
                elementOrder[5] = element2
            elif elementOrder[0] in elementList[x] and element2 in elementList[x] and elementOrder[3] in elementList[x] and elementOrder[4] in elementList[x] and elementOrder[6] in elementList[x]:
                elementOrder[2] = element2
                elementOrder[5] = element1
    return elementOrder

"""
For my own sanity, this is the logic for the function above:

Lets assume the elements are ordered from top to bottom, left to right.

We know which elements are for 1, 4, 7 and 8.

First take the elements with 2 and 3 in length. We know these are 1 and 7.
By checking the unique element, we now know the first element. We also know which
elements occupy the 3rd and 6th spots, but we don't know the order

By checking the elements with 2 and 4 in length (1 and 4), we can confirm which
2 elements are in the 2nd and 4th spots, but we don't know the order.

Using this information, we can determine which elements is 9, because out of
the unconfirmed element orders, it will contain these elements plus one extra.
Using that one extra, we can find the 7th element.

Currently, we know this:

Digits: 1, 4, 7, 8, 9
Elements: 1, 2<->4, 3<->6, 7

With this, figure out the missing element and place in into element 5, completing the
element list with a few unconfirmed spots.

We can then discover 3, as it must be one a digit order that includes elements
1, 3<->6, 7 and either one of 2 or 4 (we can check both freely, the other spot doesn't
make a digit). With this we've discovered 3, and we can also confirm the definite spots
of elements 2 and 4.

Digits: 1, 3, 4, 7, 8, 9
Elements: 1, 2, 4, 5, 3<->6, 7

In this current state, we can determine digit 0. (side note: This can be skipped)

It would be nice to confirm the last two elements, so lets do that by determining
the last two digits 2 and 5. We know that digit 2 would include elements 1, 2, 4, 6*, and 7,
so figure the odd digit out we've now confirmed element 3, and by that, also element 6.

With this we can ship this element order out.
"""

elementOrderIndex = [[0, 1, 2, 4, 5, 6], [2, 5], [0, 2, 3, 4, 6], [0, 2, 3, 5, 6], [1, 2, 3, 5], [0, 1, 3, 5, 6], [0, 1, 3, 4, 5, 6], [0, 2, 5], [0, 1, 2, 3, 4, 5, 6], [0, 1, 2, 3, 5, 6]]
def getDigitValue(elementOrder, elementList):
    digitValue = ""
    for x in range(0, len(elementList)):
        for y in range(0, len(elementOrderIndex)):
            fail = 0
            for z in range(0, len(elementOrderIndex[y])):
                if(elementOrder[elementOrderIndex[y][z]] not in elementList[x]):
                    fail = 1
            if(fail != 1 and len(elementOrderIndex[y]) == len(elementList[x])):
                digitValue += str(y)
    return int(digitValue)

input = readInput("input.txt")
digitList = []
for x in range(0, len(input)):
    splitString = input[x].split("|")
    digitList.append([splitString[0].strip().split(), splitString[1].strip().split()])

total = 0
for x in range(0, len(digitList)):
    for y in range(0, len(digitList[x][1])):
        if(len(digitList[x][1][y]) == 2 or len(digitList[x][1][y]) == 4 or len(digitList[x][1][y]) == 3 or len(digitList[x][1][y]) == 7):
            total += 1
print(total)

total = 0
for x in range(0, len(digitList)):
    elementOrder = digitElementAnalysis(digitList[x][0])
    total += getDigitValue(elementOrder, digitList[x][1])

print(total)