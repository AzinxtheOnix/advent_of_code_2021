# Used to make input reading a bit more reusable
def readInput(fileName):
    f = open(fileName, "r")
    array = []
    while(1):
        line = f.readline().replace("\n", "")
        if(line == ""):
            break
        array.append(line)
    return array