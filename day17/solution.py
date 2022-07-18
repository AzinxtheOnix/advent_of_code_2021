import sys
sys.path.append("../")

from fileRead import readInput

input = readInput("input.txt")[0]

# Code to parse the input
xLoc = input[input.find("x=")+2:input.find(",")]
yLoc = input[input.find("y=")+2:len(input)]
xLocStart = int(xLoc[0:xLoc.find("..")])
xLocEnd = int(xLoc[xLoc.find("..")+2:len(xLoc)])
yLocStart = int(yLoc[0:yLoc.find("..")])
yLocEnd = int(yLoc[yLoc.find("..")+2:len(yLoc)])

"""
yVel: Y Velocity
turns: Turns to simulate
simMode: If 1, activates a simulation mode where a x velocity is expected to be 0 over the target
"""
def simulateDetectY(yVel, turns, simMode):
    #print("Checking", yVel, "in", turns, "turns using simMode", simMode)
    yLoc = 0
    if(simMode == 1):
        curTurns = 0
        while(1):
            yLoc += yVel
            yVel -= 1
            curTurns += 1
            if(yLocStart <= yLoc and yLoc <= yLocEnd and curTurns >= turns):
                return 1
            if(yLoc < yLocStart):   # Early end case
                return 0
    else:               # Just see if the y Location is within the target area within a certain amount of turns
        for _ in range(0, turns):
            yLoc += yVel
            yVel -= 1
            if(yLoc < yLocStart):   # Early end case
                return 0
        if(yLocStart <= yLoc and yLoc <= yLocEnd):
            return 1
        return 0

def checkYList(yVel, list):
    for y in list:
        if(y == yVel):
            return 1
    return 0

"""
To find a velocity that maximizes the y location, we need an x velocity that leaves an x velocity of 0 over the target

Once we've found that, we then need to determine what y velocity maximizes the y location. This will be a velocity
that once the probe hits y=0 again, it should immediately reach the lowest target point.
"""
# First, find the first x velocity that ends with a velocity of zero right on the target
test = 0
inc = 1
xVel = -1
while(1):
    test += inc
    if(xLocStart <= test and test <= xLocEnd):
        print(inc, test)
        xVel = inc
        break
    inc += 1
    if(xLocEnd < test):
        print("End")
        break

# Key here is yLocEnd - 1 as the starting y velocity
yVel = (yLocStart * -1) - 1
print(yVel)
yLoc = 0
while(yVel != 0):
    yLoc += yVel
    yVel -= 1
print(yLoc)

"""
Now to determine the total number of inital velocities that hit the target area

We know that the miminum x velocity that hits the target area is the
first x velocity that leaves a velocity of 0 on the target

We also know that the max x velocity that hits the target area is the farthest x point on the target

So now we have a possible range of x velocities, all we have to do now is simulate each x velocity
to check if at any point it reaches the target zone, then check what y velocities are possible

We also need to check if a x velocity could strike the target twice in a run, and account for those
velocities as well ???

In order to check for possible y velocities, we know the max possible y velocity should be what was found previously
to get the highest y location.

We also know that the minimum y velocity is the lowest/farther y point on the target
"""

print("===============")

xVelMin = xVel
xVelMax = xLocEnd
yVelMin = yLocStart
yVelMax = (yLocStart * -1) - 1

print(xVelMin, xVelMax, yVelMin, yVelMax)
total = 0

for xVel in range(xVelMin, xVelMax+1):
    print(xVel, "===================")
    xLoc = 0
    turnCount = 0
    yVelList = []
    while(xLoc <= xLocEnd and xVel != 0):
        xLoc += xVel
        xVel -= 1
        turnCount += 1
        if(xLocStart <= xLoc and xLoc <= xLocEnd):
            simMode = 0
            if(xVel == 0):
                simMode = 1
            print(xLoc, turnCount, simMode)
            for yVel in range(yVelMin, yVelMax+1):
                if(simulateDetectY(yVel, turnCount, simMode) == 1 and checkYList(yVel, yVelList) == 0):
                    yVelList.append(yVel)
    print(yVelList)
    total += len(yVelList)
print(total)

