import sys

n = int(input())
OddSum = 0
OddMin = 0
OddMax = 0
EvenSum = 0
EvenMin = 0
EvenMax = 0
biggestEven = -sys.maxsize
smallestEven = sys.maxsize
biggestOdd = -sys.maxsize
smallestOdd = sys.maxsize

for i  in range(1, n + 1):
    num = float(input())
    if i % 2 == 0:
        EvenSum = EvenSum + num
        if num > biggestEven:
            EvenMax = num
            biggestEven = num
        if num < smallestEven:
            EvenMin = num
            smallestEven = num
    elif i % 2 != 0:
        OddSum = OddSum + num
        if num > biggestOdd:
            OddMax = num
            biggestOdd = num
        if num < smallestOdd:
            OddMin = num
            smallestOdd = num

            
print(f"OddSum={OddSum:.2f},")
if OddMin == 0:
    print(f"OddMin=No,")
else:
    print(f"OddMin={OddMin:.2f},")
if OddMax == 0:
    print(f"OddMax=No,")
else:
    print(f"OddMax={OddMax:.2f},")
print(f"EvenSum={EvenSum:.2f},")
if EvenMin == 0:
    print(f"EvenMin=No,")
else:
    print(f"EvenMin={EvenMin:.2f},")
if EvenMax == 0:
    print(f"EvenMax=No")
else:
    print(f"EvenMax={EvenMax:.2f}")
