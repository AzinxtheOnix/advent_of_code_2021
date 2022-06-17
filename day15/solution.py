import sys
sys.path.append("../")

from fileRead import readInput

input = readInput("input.txt")

pathNumbers = []    # The Input Map
distanceMap = []    # The Distance Map
pathList = []   # A List of Current Edges (with the shortest at the front)

# Create the input map
for x in range(0, len(input)):
    temp = []

    for y in range(0, len(input[x])):
        temp.append(int(input[x][y]))
    pathNumbers.append(temp)

iteration = 4
# Depending on how large the actual map is, adjust and fill the pathNumbers
newPathNumbers = []
for row in pathNumbers:
    temp = row.copy()
    for count in range(0, iteration):
        for col in row:
            tempNum = col+count+1
            temp.append((tempNum % 10) + (tempNum//10))
    newPathNumbers.append(temp)

length = len(newPathNumbers)
for count in range(0, iteration):
    for x in range(0, length):
        temp = []
        for col in newPathNumbers[x]:
            tempNum = col+count+1
            temp.append((tempNum % 10) + (tempNum//10))
        newPathNumbers.append(temp)

pathNumbers = newPathNumbers

maxX = len(pathNumbers)-1
maxY = len(pathNumbers[0])-1

# Create the distance map
for x in range(0, maxX+1):
    temp = [-1]*(maxY+1)
    distanceMap.append(temp.copy())

# Set the default state of pathList
pathList.append([0,0])
distanceMap[0][0] = pathNumbers[0][0]

# Function to check if a given coord is within the map
def checkValidCoord(coord):
    coordX = coord[0]
    coordY = coord[1]
    if(coordX >= 0 and coordX <= maxX and coordY >= 0 and coordY <= maxY):
        return 1
    return -1

# Function to print the distance map
def printDistanceMap():
    for row in distanceMap:
        test = ""
        for column in row:
            test += str(column) + " "
        print(test)

#printDistanceMap()

print("Completed setup, starting search")
while(1):
    #print("========================")
    # Starting Variables from arrays
    #print("Current PathList:", pathList)
    shortestCoord = pathList[0]
    coordX = shortestCoord[0]
    coordY = shortestCoord[1]
    dist = distanceMap[coordX][coordY]

    if(coordX == maxX and coordY == maxY):
        print("Found the endpoint")
        print(distanceMap[coordX][coordY]-pathNumbers[0][0])
        break

    # With the shortest path chosen, figure out which are the revealed nodes
    checkCoordList = [[coordX-1,coordY], [coordX+1,coordY], [coordX,coordY-1], [coordX,coordY+1]]
    coordList = []
    for posCoord in checkCoordList:
        posCoordX = posCoord[0]
        posCoordY = posCoord[1]
        if(checkValidCoord(posCoord) == 1 and distanceMap[posCoordX][posCoordY] == -1):

            # Place the new coord from shortest to longest distance
            pos = 0
            for x in range(0, len(coordList)):
                item = coordList[x]
                if(pathNumbers[posCoordX][posCoordY] <= pathNumbers[item[0]][item[1]]):
                    break
                else:
                    pos += 1
            coordList.insert(pos, posCoord)

            # Also, mark the coord's distance on the distance map
            distanceMap[posCoordX][posCoordY] = dist + pathNumbers[posCoordX][posCoordY]

    # Remove the first node in the pathList
    pathList.pop(0)
    #print("Cleared first item of pathList")
    #print("This is the pathList so far", pathList)
    #print("CoordList:", coordList)

    # Then place the revealed nodes in sorted order back into the pathList (also place the distance)
    if(len(pathList) == 0):
        pathList = coordList
    else:
        x = 0
        y = 0
        while(x < len(pathList) and y < len(coordList)): # Initial run through the pathList
            pathListCoord = pathList[x]
            coordListCoord = coordList[y]
            if(distanceMap[coordListCoord[0]][coordListCoord[1]] <= distanceMap[pathListCoord[0]][pathListCoord[1]]):
                pathList.insert(x, coordListCoord)
                y += 1
            else:
                x += 1
        while(y < len(coordList)): # Add any remaining items in the coordList to the end
            coordListCoord = coordList[y]
            pathList.append(coordList[y])
            y += 1
    #printDistanceMap()
    #print("This is the pathList now:", pathList)