a = int(input())
b = int(input())
max_count_pass = int(input())
counter = 0
counterA = 1
counterB = 1

while counterA <= a and counterB <= b:
    for i in range(35, 56):
        for j in range(64, 97):
                if i == 55:
                    i = 35
                if j == 96:
                    j = 64
                if counter == max_count_pass:
                    break
                print(f"{chr(i)}{chr(j)}{counterA}{counterB}{chr(j)}{chr(i)}|", end= "")
                counter += 1
                i += 1
                j += 1
                counterA += 1
                counterB += 1