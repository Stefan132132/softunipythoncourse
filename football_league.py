stadion_capacity = int(input())
fans = int(input())

fansA = 0
fansB = 0
fansG = 0
fansV = 0

for i in range(1, fans + 1):
    sector = input()
    
    if(sector == "A"):
        fansA += 1
    elif(sector == "B"):
        fansB += 1
    elif(sector == "V"):
        fansV += 1
    elif(sector == "G"):
        fansG += 1
    
procent_all = fans / stadion_capacity * 100
procentA = fansA / fans * 100
procentB = fansB / fans * 100
procentV = fansV / fans * 100
procentG = fansG / fans * 100

print(f"{procentA:.2f}%")
print(f"{procentB:.2f}%")
print(f"{procentV:.2f}%")
print(f"{procentG:.2f}%")
print(f"{procent_all:.2f}%")
