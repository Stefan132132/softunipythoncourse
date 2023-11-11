n = int(input())
l = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for g in range(97, 97 + l):
            for p in range(97, 97 + l):
                for e in range(1, n + 1):
                    if e > i and e > j:
                        print(f"{i}{j}{chr(g)}{chr(p)}{e} ", end="")