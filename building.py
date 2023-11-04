floors = int(input())
rooms_per_floor = int(input())
isLastFloor = True

for i in range(0, rooms_per_floor):
    print(f"L{floors}{i}", end= " ")
print()
floors -= 1
while floors > 0:
    if floors % 2 == 0:
        for i in range(0, rooms_per_floor):
            print(f"O{floors}{i}", end= " ")
        print()
    else:
        for i in range(0, rooms_per_floor):
            print(f"A{floors}{i}", end= " ")
        print()
    floors -= 1
        
        
    