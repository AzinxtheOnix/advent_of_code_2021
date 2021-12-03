test = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
length = len(test)

"""for x in range(0, length):
    print(test[x])
    if(x == 2):
        test.pop(x)
        length -= 1"""
x = 0
while(x < len(test)):
    print(test[x])
    if(x == 2):
        test.pop(x)
        length -= 1
    else:
        x += 1

print(int("1001", 2))