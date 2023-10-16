num = int(input())

bonus = 0

if num <= 100:
    bonus = bonus + 5
elif num > 1000:
    bonus = bonus + (0.10 * num)
else:
    bonus = bonus + (0.20 * num)
    
if num % 2 == 0:
    bonus = bonus + 1
elif num % 5 == 0 and num % 2 != 0:          #num % 10 == 5
    bonus = bonus + 2

print(bonus)
print(num + bonus)