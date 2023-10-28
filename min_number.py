number = input()
minNum = int(number)
while(number != "Stop"):
    if int(number) < minNum:
        minNum = int(number)
    number = input()
print(minNum)