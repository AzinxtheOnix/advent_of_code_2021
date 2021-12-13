import sys
import re
sys.path.append("../")

from fileRead import readInput

input = readInput("input.txt")
paperCoords = []
instructionList = []

for x in range(0, len(input)):
    if(input[x] == ""):
        break
    temp = input[x].split(",")
    paperCoords.append([int(temp[0]), int(temp[1])])

for y in range(x+1, len(input)):
    temp = input[y].split("=")
    axis = temp[0].split(" ")[2]
    coord = int(temp[1])
    instructionList.append([axis, coord])

print(paperCoords)
print(instructionList)

def fold(axis, coord):
    if(axis == "x"):
        for z in range(0, len(paperCoords)):
            if(coord < paperCoords[z][0]):
                paperCoords[z][0] = coord - (paperCoords[z][0] - coord)
    else:
        for z in range(0, len(paperCoords)):
            if(coord < paperCoords[z][1]):
                paperCoords[z][1] = coord - (paperCoords[z][1] - coord)

def organize():
    finalPaper = []
    for x in range(0, len(paperCoords)):
        bitTrigger = 0
        for y in range(0, len(finalPaper)):
            if(finalPaper[y][0] == paperCoords[x][0] and finalPaper[y][1] == paperCoords[x][1]):
                bitTrigger = 1
        if(bitTrigger == 0):
            finalPaper.append(paperCoords[x])
    return finalPaper

fold(instructionList[0][0], instructionList[0][1])
paperCoords = organize()
print(len(paperCoords))

for x in range(1, len(instructionList)):
    print("trigger")
    fold(instructionList[x][0], instructionList[x][1])
paperCoords = organize()

maxX = 0
maxY = 0
for x in range(0, len(paperCoords)):
    if(paperCoords[x][0] > maxX):
        maxX = paperCoords[x][0]
    if(paperCoords[x][1] > maxY):
        maxY = paperCoords[x][1]

display = []
for x in range(0, maxX+1):
    temp = [0] * (maxY+1)
    display.append(temp.copy())

for x in range(0, len(paperCoords)):
    display[paperCoords[x][0]][paperCoords[x][1]] = 1

for y in range(0, len(display[0])):
    printLine = ""
    for x in range(0, len(display)):
        if(display[x][y] == 0):
            printLine += "."
        else:
            printLine += "#"
    print(printLine)