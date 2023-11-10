days = int(input())
hours = int(input())

total = 0
total_all = 0

for i in range(1, days + 1):
    for j in range(1, hours + 1):
        if i % 2 != 0 and j % 2 == 0:
            total += 1.25
        elif i % 2 == 0 and j % 2 != 0:
            total += 2.50
        else:
            total += 1
    print(f"Day: {i} - {total:.2f} leva")
    total_all += total
    total = 0
print(f"Total: {total_all:.2f} leva")
        