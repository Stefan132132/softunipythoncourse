last = input()
rows_firstsector = int(input())
seats_odd = int(input())
seats_even = seats_odd + 2
counter = 0

for i in range(ord('A'), ord(last) + 1):
    rows_firstsector += 1
    for j in range(1, rows_firstsector):
        if j % 2 != 0:
            for g in range(0, seats_odd):
                print(f"{chr(i)}{j}{chr(ord('a') + g)}")
                counter += 1
        else:
            for p in range(0, seats_even):
                print(f"{chr(i)}{j}{chr(ord('a') + p)}")
                counter += 1
                
print(counter)