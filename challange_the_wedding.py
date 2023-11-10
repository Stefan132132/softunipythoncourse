men = int(input())
women = int(input())
tables = int(input())
counter = 0

for i in range(1, men + 1):
    for j in range(1, women + 1):
        if counter == tables:
            break
        print(f"({i} <-> {j})", end= " ")
        counter += 1