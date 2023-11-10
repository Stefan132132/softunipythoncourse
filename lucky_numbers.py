num = int(input())

for i in range(1, 10):
    for j in range(1, 10):
        if num % (i + j) == 0:
            for g in range(1, 10):
                for p in range(1, 10):
                    if(i + j) == (g + p):
                        print(f"{i}{j}{g}{p}", end= " ")