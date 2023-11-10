one = int(input())
two = int(input())
five = int(input())
sum_lv = int(input())

for i in range(0, one + 1):
    for j in range(0, two + 1):
        for g in range(0, five + 1):
            if i * 1 + j * 2 + g * 5 == sum_lv:
                print(f"{i} * 1 lv. + {j} * 2 lv. + {g} * 5 lv. = {sum_lv} lv.")