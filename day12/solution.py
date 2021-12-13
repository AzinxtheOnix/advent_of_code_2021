import sys
import re
sys.path.append("../")

from fileRead import readInput

input = readInput("input.txt")
caveMap = []

def checkInMap(item):
    for x in range(0, len(caveMap)):
        if(caveMap[x][0] == item):
            return caveMap[x]
    return 0

def addToMap(item):
    caveMap.append([item, []])

def addConnection(item, connection):
    for x in range(0, len(caveMap)):
        if(caveMap[x][0] == item and connection not in caveMap[x][1]):
            caveMap[x][1].append(connection)
            return 1
    return 0

def searchMap(node, target, doubleNode):
    return recursiveSearchMap(node, target, [], [], [], doubleNode, 0)

def recursiveSearchMap(node, target, previousSmallCaves, path, paths, doubleNode, doubleNodeBit):
    caveNode = checkInMap(node).copy()
    path.append(caveNode[0])
    if(len(re.findall(target, caveNode[0])) != 0):
        paths.append(path.copy())
        return paths
    if(len(re.findall("[a-z]", caveNode[0])) != 0):
        if(caveNode[0] == doubleNode and doubleNodeBit == 0):
            doubleNodeBit = 1
        else:
            previousSmallCaves.append(caveNode[0])
    for x in range(0, len(caveNode[1])):
        nextNode = caveNode[1][x]
        if(nextNode not in previousSmallCaves):
            paths = recursiveSearchMap(nextNode, target, previousSmallCaves.copy(), path.copy(), paths, doubleNode, doubleNodeBit)
    return paths

def checkIfPathMatch(path1, path2):
    if(len(path1) == len(path2)):
        for x in range(0, len(path1)):
            if(path1[x] != path2[x]):
                return 0
        return 1
    else:
        return 0

for x in range(0, len(input)):
    caves = input[x].split("-")
    item1 = caves[0]
    item2 = caves[1]
    if(checkInMap(item1) == 0):
        addToMap(item1)
    addConnection(item1, item2)
    if(checkInMap(item2) == 0):
        addToMap(item2)
    addConnection(item2, item1)

paths = searchMap("start", "end", "")
print(len(paths))

smallCave = []
for x in range(0, len(caveMap)):
    if(len(re.findall("[a-z]", caveMap[x][0])) != 0 and caveMap[x][0] != "start" and caveMap[x][0] != "end"):
        smallCave.append(caveMap[x][0])

pathList = []
for x in range(0, len(smallCave)):
    paths = searchMap("start", "end", smallCave[x])
    for y in range(0, len(paths)):
        trigger = 0
        for z in range(0, len(pathList)):
            if(checkIfPathMatch(pathList[z], paths[y]) == 1):
                trigger = 1
        if(trigger == 0):
            pathList.append(paths[y])

    #print(paths)
    #print(len(paths))
print(len(pathList))