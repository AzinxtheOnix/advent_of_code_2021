lineList = []
intersectionList = []

def checkDiagonal(line):
    if(line[0][0] != line[1][0] and line[0][1] != line[1][1]):
        return 1
    return 0

def checkHorizontal(line):
    if(line[0][1] == line[1][1]):
        return 1
    return 0

tempArray = []
for x in range(0, 1000):
    tempArray.append(0)

for x in range(0, 1000):
    intersectionList.append(tempArray.copy())

f = open("input.txt", "r")
while(1):
    line = f.readline().replace("\n", "")
    if(line == ""):
        break

    coords = line.split(" -> ")
    point1 = list(map(int, coords[0].split(",")))
    point2 = list(map(int, coords[1].split(",")))
    tempLine = [point1, point2]
    lineList.append(tempLine.copy())
f.close()

for x in range(0, len(lineList)):
    point1 = lineList[x][0]
    point2 = lineList[x][1]
    if(checkDiagonal(lineList[x]) == 1):
        pass
    elif(checkHorizontal(lineList[x]) == 1):
        if(point1[0] > point2[0]):
            for x in range(point2[0], point1[0]+1):
                intersectionList[x][point1[1]] += 1
        else:
            for x in range(point1[0], point2[0]+1):
                intersectionList[x][point1[1]] += 1

    else:
        if(point1[1] > point2[1]):
            for x in range(point2[1], point1[1]+1):
                intersectionList[point1[0]][x] += 1
        else:
            for x in range(point1[1], point2[1]+1):
                intersectionList[point1[0]][x] += 1

counter = 0
for x in range(0, len(intersectionList)):
    for y in range(0, len(intersectionList[x])):
        if(intersectionList[x][y] > 1):
            counter += 1
print(counter)

# Part 2
intersectionList.clear()
for x in range(0, 1000):
    intersectionList.append(tempArray.copy())

for x in range(0, len(lineList)):
    point1 = lineList[x][0]
    point2 = lineList[x][1]
    if(checkDiagonal(lineList[x]) == 1):
        if(point1[0] < point2[0]):      # Point1's x is smaller
            if(point1[1] < point2[1]):          # Counting up
                y = 0
                for x in range(point1[0], point2[0]+1):
                    intersectionList[x][point1[1]+y] += 1
                    y += 1
            else:                               # Counting down
                y = 0
                for x in range(point1[0], point2[0]+1):
                    intersectionList[x][point1[1]+y] += 1
                    y -= 1

        else:                           # Point2's x is smaller
            if(point2[1] < point1[1]):
                y = 0
                for x in range(point2[0], point1[0]+1):
                    intersectionList[x][point2[1]+y] += 1
                    y += 1
            else:
                y = 0
                for x in range(point2[0], point1[0]+1):
                    intersectionList[x][point2[1]+y] += 1
                    y -= 1

    elif(checkHorizontal(lineList[x]) == 1):
        if(point1[0] > point2[0]):
            for x in range(point2[0], point1[0]+1):
                intersectionList[x][point1[1]] += 1
        else:
            for x in range(point1[0], point2[0]+1):
                intersectionList[x][point1[1]] += 1

    else:
        if(point1[1] > point2[1]):
            for x in range(point2[1], point1[1]+1):
                intersectionList[point1[0]][x] += 1
        else:
            for x in range(point1[1], point2[1]+1):
                intersectionList[point1[0]][x] += 1

counter = 0
for x in range(0, len(intersectionList)):
    for y in range(0, len(intersectionList[x])):
        if(intersectionList[x][y] > 1):
            counter += 1
print(counter)