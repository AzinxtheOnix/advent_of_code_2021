import sys
sys.path.append("../")

from fileRead import readInput

input = readInput("input.txt")
fishTimer = list(map(int, input[0].split(",")))
print(len(fishTimer))

lifeList = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for x in range(0, len(fishTimer)):      # To be used in part 2
    lifeList[fishTimer[x]] += 1

# print("Initial State:   ", fishTimer)
for x in range(0, 80):
    for y in range(0, len(fishTimer)):
        if(fishTimer[y] == 0):
            fishTimer[y] = 6
            fishTimer.append(8)
        else:
            fishTimer[y] -= 1
    # print("After", x, "Days:    ", fishTimer)

print(len(fishTimer))

# Now the challenge is optimizing it for a run of 256

for x in range(0, 256):
    tempArray = lifeList.copy()
    for y in range(1, len(lifeList)):
        lifeList[y-1] = tempArray[y]
    lifeList[8] = tempArray[0]
    lifeList[6] += tempArray[0]

total = 0
for x in range(0, len(lifeList)):
    total += lifeList[x]
print(total)