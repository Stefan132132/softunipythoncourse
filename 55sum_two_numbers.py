start = int(input())
end = int(input())
combination_sum = int(input())
counter_combinations = 0
shouldBreak = False

for i in range(start, end + 1):
    for j in range(start, end + 1):
        counter_combinations += 1
        if i + j == combination_sum:
            shouldBreak = True
            break
    if shouldBreak:
        break
        
if shouldBreak:
    print(f"Combination N:{counter_combinations} ({i} + {j} = {combination_sum})")
else:
    print(f"{counter_combinations} combinations - neither equals {combination_sum}")