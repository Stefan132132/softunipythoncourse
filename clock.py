mins = 0
hour = 0

for i in range(0,24):
    for j in range(0, 60):
        print(f"{hour} : {mins:0d}")
        mins = mins + 1
        if mins == 60:
            mins = 0
    hour = hour + 1