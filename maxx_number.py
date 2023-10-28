number = input()
maxNum = int(number)
while(number != "Stop"):
    if int(number) > maxNum:
        maxNum = int(number)
    number = input()
print(maxNum)