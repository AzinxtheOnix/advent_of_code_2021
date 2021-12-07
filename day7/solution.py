import sys
sys.path.append("../")

from fileRead import readInput

def findFuelCost(location, locationList):
    fuel = 0
    for x in range(0, len(locationList)):
        fuel += abs(locationList[x] - location)
    return fuel

def findFuelCostImproved(location, locationList):
    fuel = 0
    for x in range(0, len(locationList)):
        counter = abs(locationList[x] - location)
    
        increment = 1
        for y in range(0, counter):
            fuel += increment
            increment += 1

    return fuel

input = readInput("input.txt")
crabLocations = list(map(int, input[0].split(",")))
crabLocations.sort()

"""
The following chunk of code is only viable for a small sample size
But I noticed that if we were to sort the numbers in order and check the cost of moving to that postion, there is some
point where the fuel costs will be the lowest, and will start growing to both sides
What if we could use binary search to find this location?
"""
"""for x in range(crabLocations[0], crabLocations[-1]+1):
    print("Testing:", x, "as a possible coordinate")
    fuel = 0
    for y in range(0, len(crabLocations)):
        fuel += abs(crabLocations[y] - x)
    print(fuel)
"""

lowRange = crabLocations[0]
highRange = crabLocations[-1]
median = (lowRange + highRange) // 2
while(1):
    cost1 = findFuelCost(median-1, crabLocations)
    cost2 = findFuelCost(median, crabLocations)
    cost3 = findFuelCost(median+1, crabLocations)

    if(cost1 < cost2 and cost2 < cost3):
        highRange = median
        median = (lowRange + highRange) // 2
    elif(cost1 > cost2 and cost2 > cost3):
        lowRange = median
        median = (lowRange + highRange) // 2
    else:
        print(cost2)
        break

lowRange = crabLocations[0]
highRange = crabLocations[-1]
median = (lowRange + highRange) // 2
while(1):
    cost1 = findFuelCostImproved(median-1, crabLocations)
    cost2 = findFuelCostImproved(median, crabLocations)
    cost3 = findFuelCostImproved(median+1, crabLocations)
    
    if(cost1 < cost2 and cost2 < cost3):
        highRange = median
        median = (lowRange + highRange) // 2
    elif(cost1 > cost2 and cost2 > cost3):
        lowRange = median
        median = (lowRange + highRange) // 2
    else:
        print(cost2)
        break