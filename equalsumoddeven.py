first_num = int(input())
second_num = int(input())

for i in range(first_num, second_num + 1):
    number_as_str = str(i)
    even_sum = 0
    odd_sum = 0
    
    for index, digit in enumerate(number_as_str):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
            
    if even_sum == odd_sum:
        print(i, end=" ")
print()