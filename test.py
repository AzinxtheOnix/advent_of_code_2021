"""
pathNumbers = []
for x in range(0, 11):
    temp = [-1]*(11)
    pathNumbers.append(temp.copy())

checkCoordList = [[0,0], [0,1], [0,2], [0,3]]
coordList = []
for posCoord in checkCoordList:
    posCoordX = posCoord[0]
    posCoordY = posCoord[1]

    # Place the new coord from shortest to longest distance
    pos = 0
    for x in range(0, len(coordList)):
        item = coordList[x]
        if(pathNumbers[posCoordX][posCoordY] <= pathNumbers[item[0]][item[1]]):
            break
        else:
            pos += 1
    coordList.insert(pos, posCoord)
"""
"""
#testArray = [0, 2, 4, 6, 8]
testArray = []
array = [1, 3, 4, 5, 7, 9]
if(len(testArray) == 0):
    testArray = array
else:
    x = 0
    y = 0
    while(x < len(testArray) and y < len(array)):
        if(array[y] <= testArray[x]):
            testArray.insert(x, array[y])
            y += 1
        else:
            x += 1
    while(y < len(array)):
        testArray.insert(x, array[y])
        y += 1

print(testArray)
"""
tempNum = 25
print((tempNum % 10) + (tempNum//10))
