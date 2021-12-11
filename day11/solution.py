import sys
sys.path.append("../")

from fileRead import readInput

input = readInput("input.txt")
octoMap = []

for x in range(0, len(input)):
    octoMap.append([])
    for y in range(0, len(input[x])):
        octoMap[x].append(int(input[x][y]))

def incSpaces():
    for x in range(0, len(octoMap)):
        for y in range(0, len(octoMap[x])):
            octoMap[x][y] += 1

def flashSpace():
    previousLocations = []
    for x in range(0, len(octoMap)):
        for y in range(0, len(octoMap[x])):
            previousLocations = flashSpaces([x, y], previousLocations.copy())
    return previousLocations

def flashSpaces(updateLocation, previousLocations):
    x = updateLocation[0]
    y = updateLocation[1]

    if(octoMap[x][y] > 9 and [x, y] not in previousLocations):
        previousLocations.append([x, y])
        pulseMap = [[x-1, y-1], [x-1, y], [x-1, y+1], [x, y-1], [x, y+1], [x+1, y-1], [x+1, y], [x+1, y+1]]
        for pos in range(0, len(pulseMap)):
            next_x = pulseMap[pos][0]
            next_y = pulseMap[pos][1]
            if(0 <= next_x and next_x <= len(octoMap)-1 and 0 <= next_y and next_y <= len(octoMap[x])-1):
                octoMap[next_x][next_y] += 1
                previousLocations = flashSpaces([next_x, next_y], previousLocations)
    return previousLocations

def resetSpaces():
    for x in range(0, len(octoMap)):
        for y in range(0, len(octoMap[x])):
            if(octoMap[x][y] > 9):
                octoMap[x][y] = 0

def printMap():     # Only used for debugging purposes
    for x in range(0, len(octoMap)):
        string = ""
        for y in range(0, len(octoMap[x])):
            string += str(octoMap[x][y])
        print(string)
    print("==============")

def checkSync():
    for x in range(0, len(octoMap)):
        for y in range(0, len(octoMap[x])):
            if(octoMap[x][y] != 0):
                return 0
    return 1

count = 0
countTo = 100
for inc in range(0, countTo):
    incSpaces()
    count += len(flashSpace())
    resetSpaces()
    if(checkSync() == 1):
        sync = inc+1
print(count)

sync = -1
inc = countTo
while(sync == -1):
    incSpaces()
    count += len(flashSpace())
    resetSpaces()
    if(checkSync() == 1):
        sync = inc+1
    inc += 1
print(sync)