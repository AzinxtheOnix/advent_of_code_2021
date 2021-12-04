def searchNumbers(num, numberList):
    for x in range(0, len(numberList)):
        if (num == numberList[x]):
            return 1
    return 0

def checkCard(card, currentNumbers):
    for x in range(0, 5):               # Check the horizontal rows
        for y in range(0, 5):
            if(searchNumbers(card[x][y], currentNumbers) == 0):
                break
            if(y == 4):
                print("Row:", x)
                return 1
    
    for x in range(0, 5):               # Check the vertical columns
        for y in range(0, 5):
            if(searchNumbers(card[y][x], currentNumbers) == 0):
                break
            if(y == 4):
                print("Col:", x)
                return 1
    
    return 0

def calculateResult(card, currentNumbers):
    unmarkedSum = 0
    for x in range(0, 5):
        for y in range(0, 5):
            if(searchNumbers(card[x][y], currentNumbers) == 0):
                unmarkedSum += card[x][y]

    return unmarkedSum * currentNumbers[-1]

f = open("input.txt", "r")
numberOrderString = f.readline().replace("\n", "")
numberOrder = list(map(int, numberOrderString.split(",")))
f.readline()

bingoCards = [[]]
count = 0

while f:
    line = f.readline()
    
    if(line == ""):
        break
    if(line != "\n"):
        bingoCards[count].append(list(map(int, line.replace("\n", "").split()))) # A bit complex here, basically translates each line to integer
    else:
        bingoCards.append([])
        count += 1

print(numberOrder)
for x in range(0, len(bingoCards)):
    print(bingoCards[x])

currentNumber = 0
pulledNumbers = []
bingoStatus = 1

while(bingoStatus):
    pulledNumbers.append(numberOrder[currentNumber])
    currentNumber += 1
    
    print(pulledNumbers)

    for x in range(0, len(bingoCards)):
        if(checkCard(bingoCards[x], pulledNumbers) == 1):
            print("Found the card:")
            print(bingoCards[x])
            print(calculateResult(bingoCards[x], pulledNumbers))
            bingoStatus = 0
            break

currentNumber = 0
pulledNumbers = []
bingoStatus = 0

while(1):
    if(currentNumber == len(numberOrder)):
        break
    pulledNumbers.append(numberOrder[currentNumber])
    currentNumber += 1
    
    # print(pulledNumbers)
    # print(len(bingoCards))
    
    x = 0
    while(x < len(bingoCards)):
        if(len(bingoCards) == 1):
            bingoStatus = 1
        if(checkCard(bingoCards[x], pulledNumbers) == 1):
            if(bingoStatus == 1):
                print("Found the loser:")
                print(calculateResult(bingoCards[x], pulledNumbers))
            bingoCards.pop(x)
        else:
            x += 1

for x in range(0, len(bingoCards)):
    print(bingoCards[x])
    print(checkCard(bingoCards[x], pulledNumbers))