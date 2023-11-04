beginning = int(input())
end = int(input())
magic_number = int(input())
comb_counter = 0
isCombFound = False


for d in range(beginning, end + 1):
    for z in range(beginning, end + 1):
        comb_counter += 1
        if d + z == magic_number:
            isCombFound = True
            break
    if isCombFound:
        break
if isCombFound:
    print(f"Combination N:{comb_counter} ({d} + {z} = {magic_number})")
else:
    print(f"{comb_counter} combinations - neither equals {magic_number}")