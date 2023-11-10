start = int(input())
end = int(input())

for i in range(start, end + 1):
        for j in range(start, end + 1):
            for g in range(start, end + 1):
                for p in range(start, end + 1):
                    if(i % 2 == 0 and p % 2 != 0 and i > p and (j + g) % 2 == 0):
                        print(f"{i}{j}{g}{p}", end=" ")
                    elif(i % 2 != 0 and p % 2 == 0 and i > p and (j + g) % 2 ==0):
                        print(f"{i}{j}{g}{p}", end=" ")
            