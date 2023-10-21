import sys
n = int(input())
maxNum = -sys.maxsize
sum1 = 0

for i in range(0, n):
    num = int(input())
    if num > maxNum:
        maxNum = num
    sum1 = sum1 + num
    
if maxNum == sum1 - maxNum:
    print("Yes")
    print(f"Sum = {maxNum}")
else:
    print("No")
    sum1 = sum1 - maxNum
    print(f"Diff = {abs(maxNum - sum1)}")