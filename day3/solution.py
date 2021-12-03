zero_bit_counter_p1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
one_bit_counter_p1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
potential_oxygen_rating = []
potential_CO2_rating = []

f = open("input.txt", "r")
while(1):
    line = f.readline().replace("\n", "")
    if(line == ""):
        break

    potential_oxygen_rating.append(line)        # For the part 2 later
    potential_CO2_rating.append(line)

    for x in range(0, len(line)):
        if(int(line[x]) == 0):
            zero_bit_counter_p1[x] += 1
        else:
            one_bit_counter_p1[x] += 1

print(zero_bit_counter_p1)
print(one_bit_counter_p1)

gammaStringBin = "0b"

for x in range(0, len(zero_bit_counter_p1)):
    if(zero_bit_counter_p1[x] > one_bit_counter_p1[x]):
        gammaStringBin += "0"
    else:
        gammaStringBin += "1"

print(gammaStringBin)
gammaValue = int(gammaStringBin, 2)
epsilonValue = gammaValue ^ 0b111111111111

print(gammaValue)
print(epsilonValue)
print(gammaValue * epsilonValue)

for x in range(0, 12):
    if(len(potential_oxygen_rating) == 1):
        break
    else:
        commonBit = 0
        zero_bit_counter_p2 = 0
        one_bit_counter_p2 = 0

        for y in range(0, len(potential_oxygen_rating)):
            if(int(potential_oxygen_rating[y][x]) == 0):
                zero_bit_counter_p2 += 1
            else:
                one_bit_counter_p2 += 1

        if(zero_bit_counter_p2 <= one_bit_counter_p2):
            commonBit = 1
        
        y = 0
        while(y < len(potential_oxygen_rating)):
            if(int(potential_oxygen_rating[y][x]) != commonBit):
                potential_oxygen_rating.pop(y)
            else:
                y += 1

for x in range(0, 12):
    if(len(potential_CO2_rating) == 1):
        break
    else:
        leastBit = 1
        zero_bit_counter_p2 = 0
        one_bit_counter_p2 = 0

        for y in range(0, len(potential_CO2_rating)):
            if(int(potential_CO2_rating[y][x]) == 0):
                zero_bit_counter_p2 += 1
            else:
                one_bit_counter_p2 += 1

        if(zero_bit_counter_p2 <= one_bit_counter_p2):
            leastBit = 0
        
        y = 0
        while(y < len(potential_CO2_rating)):
            if(int(potential_CO2_rating[y][x]) != leastBit):
                potential_CO2_rating.pop(y)
            else:
                y += 1

print(potential_oxygen_rating)
print(potential_CO2_rating)

print(int(potential_oxygen_rating[0],2) * int(potential_CO2_rating[0],2))