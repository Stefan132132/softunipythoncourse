n = int(input())
sum_nums = 0
for i in range(0, n):
    num = int(input())
    sum_nums = sum_nums + num
print(f"{(sum_nums / n):.2f}")