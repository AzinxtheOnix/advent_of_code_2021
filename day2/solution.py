import sys

def part1():
    horizontalPos = 0
    depth = 0

    f = open("input.txt", "r")
    while(1):
        line = f.readline().replace("\n", "")
        if(line == ""):
            break
        
        mov_inc = line.split()
        move = mov_inc[0]
        increment = int(mov_inc[1])

        if(move == "forward"):               # Still wish there was switch statements
            horizontalPos += increment
        elif(move == "up"):
            depth -= increment
        else:   # Must be down
            depth += increment
    
    print(horizontalPos*depth)

def part2():
    horizontalPos = 0
    depth = 0
    aim = 0

    f = open("input.txt", "r")
    while(1):
        line = f.readline().replace("\n", "")
        if(line == ""):
            break
        
        mov_inc = line.split()
        move = mov_inc[0]
        increment = int(mov_inc[1])

        if(move == "forward"):               # Still wish there was switch statements
            horizontalPos += increment
            depth += aim*increment
        elif(move == "up"):
            aim -= increment
        else:   # Must be down
            aim += increment
    
    print(horizontalPos*depth)

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