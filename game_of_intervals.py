turns = int(input())
interval1 = 0
interval2 = 0
interval3 = 0
interval4 = 0
interval5 = 0
invalid_nums = 0

points = 0

for i in range(1, turns + 1):
    number = int(input())
    
    if 0 <= number <= 9:
        points = points + (0.20 * number)
        interval1 += 1
    elif 10 <= number <= 19:
        points = points + (0.30 * number)
        interval2 += 1
    elif 20 <= number <= 29:
        points = points + (0.40 * number)
        interval3 += 1
    elif 30 <= number <= 39:
        points = points + 50
        interval4 += 1
    elif 40 <= number <= 50:
        points = points + 100
        interval5 += 1
    else:
        points = points / 2
        invalid_nums += 1
    
print(f"{points:.2f}")
print(f"From 0 to 9: {(interval1/turns*100):.2f}%")
print(f"From 10 to 19: {(interval2/turns*100):.2f}%")
print(f"From 20 to 29: {(interval3/turns*100):.2f}%")
print(f"From 30 to 39: {(interval4/turns*100):.2f}%")
print(f"From 40 to 50: {(interval5/turns*100):.2f}%")
print(f"Invalid numbers: {(invalid_nums/turns*100):.2f}%")
    
    