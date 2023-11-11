number = input()
first_digit = int(number[0])
second_digit = int(number[1])
third_digit = int(number[2])

for i in range(1, third_digit + 1):
    for j in range(1, second_digit + 1):
        for g in range(1, first_digit + 1):
            print(f"{i} * {j} * {g} = {i * j * g};")
