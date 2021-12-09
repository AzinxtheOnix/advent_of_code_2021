import sys
sys.path.append("../")

from fileRead import readInput

input = readInput("input.txt")

listofLow = []
total = 0

for x in range(0, len(input)):
    for y in range(0, len(input[x])):
        highStatus = 0
        if(x != 0 and int(input[x-1][y]) <= int(input[x][y])):
            highStatus += 1
        if(x != len(input)-1 and int(input[x+1][y]) <= int(input[x][y])):
            highStatus += 1
        if(y != 0 and int(input[x][y-1]) <= int(input[x][y])):
            highStatus += 1
        if(y != len(input[x])-1 and int(input[x][y+1]) <= int(input[x][y])):
            highStatus += 1
        
        if(highStatus == 0):
            listofLow.append([x, y].copy())
            total += int(input[x][y]) + 1
            
print(total)

def recursiveSearch(currentLocation, travelledLocations, map):
    x = currentLocation[0]
    y = currentLocation[1]
    
    travelledLocations.append([x, y].copy())
    if(x != 0 and int(map[x-1][y]) > int(map[x][y]) and int(map[x-1][y]) != 9 and ([x-1, y] not in travelledLocations)):
        travelledLocations = recursiveSearch([x-1, y], travelledLocations, map)
    if(x != len(map)-1 and int(map[x+1][y]) > int(map[x][y]) and int(map[x+1][y]) != 9 and ([x+1, y] not in travelledLocations)):
        travelledLocations = recursiveSearch([x+1, y], travelledLocations, map)
    if(y != 0 and int(map[x][y-1]) > int(map[x][y]) and int(map[x][y-1]) != 9 and ([x, y-1] not in travelledLocations)):
        travelledLocations = recursiveSearch([x, y-1], travelledLocations, map)
    if(y != len(map[x])-1 and int(map[x][y+1]) > int(map[x][y]) and int(map[x][y+1]) != 9 and ([x, y+1] not in travelledLocations)):
        travelledLocations = recursiveSearch([x, y+1], travelledLocations, map)

    return travelledLocations

test = []
for x in range(0, len(listofLow)):
    test.append(len(recursiveSearch(listofLow[x], [], input)))
test.sort()
print(test[-1] * test[-2] * test[-3])