import sys
sys.path.append("../")

from fileRead import readInput

input = readInput("input.txt")
corruptedCount = [0, 0, 0, 0]
incompleteScores = []

for x in range(0, len(input)):
    codeStack = []
    corrupted = 0
    for y in range(0, len(input[x])):
        if(input[x][y] == "{" or input[x][y] == "<" or input[x][y] == "(" or input[x][y] == "["):
            codeStack.append(input[x][y])
        else:
            codeChar = codeStack.pop()
            if(input[x][y] == "}" and codeChar != "{"):
                corruptedCount[2] += 1
                corrupted = 1
                break
            if(input[x][y] == ">" and codeChar != "<"):
                corruptedCount[3] += 1
                corrupted = 1
                break
            if(input[x][y] == "]" and codeChar != "["):
                corruptedCount[1] += 1
                corrupted = 1
                break
            if(input[x][y] == ")" and codeChar != "("):
                corruptedCount[0] += 1
                corrupted = 1
                break
    if(corrupted == 0):
        score = 0
        while(len(codeStack) != 0):
            score *= 5
            codeChar = codeStack.pop()
            if(codeChar == "{"):
                score += 3
            if(codeChar == "<"):
                score += 4
            if(codeChar == "["):
                score += 2
            if(codeChar == "("):
                score += 1
        incompleteScores.append(score)

print(corruptedCount[0]*3 + corruptedCount[1]*57 + corruptedCount[2]*1197 + corruptedCount[3]*25137)
incompleteScores.sort()
print(incompleteScores[len(incompleteScores)//2])