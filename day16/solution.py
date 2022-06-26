import sys
sys.path.append("../")

from fileRead import readInput

input = readInput("input.txt")[0]

hexValues = ['0', '1', '2', '3',
            '4', '5', '6', '7',
            '8', '9', 'A', 'B',
            'C', 'D', 'E', 'F']
hexMap = ["0000", "0001", "0010", "0011",
        "0100", "0101", "0110", "0111",
        "1000", "1001", "1010", "1011",
        "1100", "1101", "1110", "1111"]

binaryInput = ""
for char in input:
    index = hexValues.index(char)
    binaryInput += hexMap[index]

def readBytes(binReadLoc, length):
    return (binaryInput[binReadLoc:binReadLoc+length], binReadLoc+length)

def decodeBinary(binaryVal):
    return int(binaryVal, 2)

def sumOperator(values):
    total = 0
    for number in values:
        total += number
    return total

def productOperator(values):
    total = -1
    for number in values:
        if(total == -1):
            total = number
        else:
            total *= number
    return total

def minOperator(values):
    val = -1
    for number in values:
        if(val == -1 or number < val):
            val = number
    return val

def maxOperator(values):
    val = -1
    for number in values:
        if(val == -1 or number > val):
            val = number
    return val

def greaterThanOperator(values):
    if(values[0] > values[1]):
        return 1
    return 0

def lessThanOperator(values):
    if(values[0] < values[1]):
        return 1
    return 0

def equalToOperator(values):
    if(values[0] == values[1]):
        return 1
    return 0

operatorValues = [0, 1, 2, 3, 5, 6, 7]

operatorFunctionMap = [sumOperator, productOperator,
                        minOperator, maxOperator,
                        greaterThanOperator, lessThanOperator,
                        equalToOperator]

"""
Parameters:
binaryReadLocation

Returns these properties:
Packet Version Total
Number Total
binaryNextReadLocation
"""
def readLiteralPacket(binReadLoc):
    binaryResult = ""
    while(1):
        rawBytes, binReadLoc = readBytes(binReadLoc, 5)
        binaryResult += rawBytes[1:]
        if(decodeBinary(rawBytes[0]) == 0):
            break
    number = decodeBinary(binaryResult)
    return (0, number, binReadLoc)

"""
Parameters:
packetTypeID
binaryReadLocation

Returns these properties:
Packet Version Total
Number Total
binaryNextReadLocation
"""
def readOperatorPacket(packetTypeID, binReadLoc):
    lengthTypeID, binReadLoc = readBytes(binReadLoc, 1)
    packetVerTol = 0
    numberArray = []
    if(decodeBinary(lengthTypeID) == 0):        # Decode as byte length
        bytesReadLimit, binReadLoc = readBytes(binReadLoc, 15)
        bytesReadLimit = decodeBinary(bytesReadLimit)
        currentBytesRead = 0
        while(1):
            info = readPacketHeader(binReadLoc)
            packetVerTol += info[0]
            numberArray.append(info[1])
            newBinReadLoc = info[2]
            currentBytesRead += newBinReadLoc - binReadLoc
            binReadLoc = newBinReadLoc
            if(currentBytesRead >= bytesReadLimit):         # Should never reach the greater than case
                break
    else:                                       # Decode as number of packets
        packetReadLimit, binReadLoc = readBytes(binReadLoc, 11)
        packetReadLimit = decodeBinary(packetReadLimit)
        currentPacketsRead = 0
        while(1):
            info = readPacketHeader(binReadLoc)
            packetVerTol += info[0]
            numberArray.append(info[1])
            binReadLoc = info[2]
            currentPacketsRead += 1
            if(currentPacketsRead == packetReadLimit):
                break
    
    # Now to deal with the numberTotal
    operLoc = operatorValues.index(packetTypeID)
    numberTol = operatorFunctionMap[operLoc](numberArray)

    return (packetVerTol, numberTol, binReadLoc)

"""
Parameters:
binaryReadLocation

Returns these properties:
Packet Version Total
Number Total
binaryNextReadLocation
"""
def readPacketHeader(binReadLoc):
    packetVerTol, binReadLoc = readBytes(binReadLoc, 3)
    packetVerTol = decodeBinary(packetVerTol)
    packetTypeID, binReadLoc = readBytes(binReadLoc, 3)
    packetTypeID = decodeBinary(packetTypeID)
    if(packetTypeID == 4):
        info = readLiteralPacket(binReadLoc)
    else:
        info = readOperatorPacket(packetTypeID, binReadLoc)

    packetVerTol += info[0]
    numberTol = info[1]
    binReadLoc = info[2]
    return (packetVerTol, numberTol, binReadLoc)

print(readPacketHeader(0))