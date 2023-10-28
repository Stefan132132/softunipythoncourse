mins = 0
hour = 0
seconds = 0

for i in range(0,24):
    for j in range(0, 60):
        for g in range(0, 60):
            print(f"{hour} : {mins} : {seconds}")
            seconds = seconds + 1
            if seconds == 60:
                seconds = 0
        mins = mins + 1
        if mins == 60:
            mins = 0
    hour = hour + 1