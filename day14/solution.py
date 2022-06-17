import sys
sys.path.append("../")

from fileRead import readInput

input = readInput("input.txt")
polymerList = []
polymerRules = []
runningList = []

for x in range(0, len(input[0])):
    polymerList.append(input[0][x])

for x in range(2, len(input)):
    temp = input[x].split(" -> ")
    polymerRules.append([[temp[0][0], temp[0][1]], temp[1]])

def checkInRunningList(item1, item2, runList):
    for x in range(0, len(runList)):
        if(runList[x][0][0] == item1 and runList[x][0][1] == item2):
            return x
    return -1

def findRule(item1, item2):
    for x in range(0, len(polymerRules)):
        if(polymerRules[x][0][0] == item1 and polymerRules[x][0][1] == item2):
            return polymerRules[x][1]

polymer1 = polymerList[0]
polymer2 = polymerList[-1]

for x in range(0, len(polymerList)-1):
    status = checkInRunningList(polymerList[x], polymerList[x+1], runningList)
    if(status == -1):
        runningList.append([[polymerList[x], polymerList[x+1]], 1])
    else:
        runningList[status][1] += 1

depth1 = 10
for x in range(0, depth1):
    newRunningList = []
    for y in range(0, len(runningList)):
        item1 = runningList[y][0][0]
        item2 = runningList[y][0][1]
        amount = runningList[y][1]

        charResult = findRule(item1, item2)

        status = checkInRunningList(item1, charResult, newRunningList)
        if(status == -1):
            newRunningList.append([[item1, charResult], amount])
        else:
            newRunningList[status][1] += amount
        
        status = checkInRunningList(charResult, item2, newRunningList)
        if(status == -1):
            newRunningList.append([[charResult, item2], amount])
        else:
            newRunningList[status][1] += amount
        
    runningList = newRunningList

def checkInCount(item, countList):
    for x in range(0, len(countList)):
        if(item == countList[x][0]):
            return x
    return -1

totalCount = []
for x in range(0, len(runningList)):
    item1 = runningList[x][0][0]
    item2 = runningList[x][0][1]
    count = runningList[x][1]
    
    status = checkInCount(item1, totalCount)
    if(status != -1):
        totalCount[status][1] += count
    else:
        totalCount.append([item1, count])

    status = checkInCount(item2, totalCount)
    if(status != -1):
        totalCount[status][1] += count
    else:
        totalCount.append([item2, count])

high = -1
low = -1
for x in range(0, len(totalCount)):
    totalCount[x][1] //= 2
    if(totalCount[x][0] == polymer1 or totalCount[x][0] == polymer2):
        totalCount[x][1] += 1
    
    if(high == -1):
        high = totalCount[x][1]
        low = totalCount[x][1]
    
    if(totalCount[x][1] > high):
        high = totalCount[x][1]
    if(totalCount[x][1] < low):
        low = totalCount[x][1]
print(high - low)

depth2 = 40
for x in range(0, depth2 - depth1):
    newRunningList = []
    for y in range(0, len(runningList)):
        item1 = runningList[y][0][0]
        item2 = runningList[y][0][1]
        amount = runningList[y][1]

        charResult = findRule(item1, item2)

        status = checkInRunningList(item1, charResult, newRunningList)
        if(status == -1):
            newRunningList.append([[item1, charResult], amount])
        else:
            newRunningList[status][1] += amount
        
        status = checkInRunningList(charResult, item2, newRunningList)
        if(status == -1):
            newRunningList.append([[charResult, item2], amount])
        else:
            newRunningList[status][1] += amount
        
    runningList = newRunningList

totalCount = []
for x in range(0, len(runningList)):
    item1 = runningList[x][0][0]
    item2 = runningList[x][0][1]
    count = runningList[x][1]
    
    status = checkInCount(item1, totalCount)
    if(status != -1):
        totalCount[status][1] += count
    else:
        totalCount.append([item1, count])

    status = checkInCount(item2, totalCount)
    if(status != -1):
        totalCount[status][1] += count
    else:
        totalCount.append([item2, count])

high = -1
low = -1
for x in range(0, len(totalCount)):
    totalCount[x][1] //= 2
    if(totalCount[x][0] == polymer1 or totalCount[x][0] == polymer2):
        totalCount[x][1] += 1
    
    if(high == -1):
        high = totalCount[x][1]
        low = totalCount[x][1]
    
    if(totalCount[x][1] > high):
        high = totalCount[x][1]
    if(totalCount[x][1] < low):
        low = totalCount[x][1]
print(high - low)