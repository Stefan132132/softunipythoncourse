a = int(input())
b = int(input())
max_count_pass = int(input())
counter = 1
shouldBreak = False
i = 35
j = 64


for g in range(1, a + 1):
    for p in range(1, b + 1):
        if g == a and p == b:
            shouldBreak = True
        if i > 55:
            i = 35
        if j > 96:
            j = 64
        print(f"{chr(i)}{chr(j)}{g}{p}{chr(j)}{chr(i)}|", end= "")
        if counter == max_count_pass:
            shouldBreak = True
            break
        counter += 1
        i += 1
        j += 1
    if shouldBreak:
        break

        
    
                
        