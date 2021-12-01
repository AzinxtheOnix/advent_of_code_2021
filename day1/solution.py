import sys

def part1():                    # I think this goes without saying, but I wish there was the ability to use {} in python
    f = open("input", "r")
    item1 = int(f.readline().replace("\n", ""))
    counter = 0
    
    while(1):
        line = f.readline().replace("\n", "")
        if(line == ""):
            break
        item2 = int(line)
        if(item1 < item2):
            counter += 1
        item1 = item2

    print(counter)

def part2():
    f = open("input", "r")
    item1 = int(f.readline().replace("\n", ""))
    item2 = int(f.readline().replace("\n", ""))
    item3 = int(f.readline().replace("\n", ""))
    counter = 0
    
    while(1):
        line = f.readline().replace("\n", "")
        if(line == ""):
            break
        item4 = int(line)
        if(item1 + item2 + item3 < item2 + item3 + item4):
            counter += 1
        item1 = item2
        item2 = item3
        item3 = item4

    print(counter)

if(len(sys.argv) == 1):         # Why is the and/or operators in python the actual words instead of || and &&...
    print("No arguments found, defaulting to part 1")
    part1()
elif(sys.argv[1] == "1"):
    print("Activating part 1")
    part1()
elif(sys.argv[1] == "2"):
    print("Activating part 2")
    part2()
else:                           # And why isn't there a switch case in python...
    print("No valid arguments, defaulting to part 1")
    part1()