hour_exam = int(input())
minutes_exam = int(input())
hour_arrived = int(input())
minutes_arrived = int(input())

allminutes_exam = hour_exam * 60 + minutes_exam
allminutes_arrived = hour_arrived * 60 + minutes_arrived
mins = allminutes_exam - allminutes_arrived
mins2 = allminutes_arrived - allminutes_exam

if allminutes_exam == allminutes_arrived or mins <= 30 and mins > 0:
    if mins > 0:
        print("On time")
        print(f"{mins} minutes before the start")
    print("On time")
    
elif mins > 30 and mins < 60:
    print("Early")
    print(f"{mins} minutes before the start")
elif mins2 > 0 and mins2 < 60:
    print("Late")
    print(f"{mins2} minutes after the start")
elif mins > 30 and mins >= 60:
    hour = mins // 60
    minutes = mins % 60
    print("Early")
    print(f"{hour}:{minutes:02d} hours before the start")
elif mins2 > 0 and mins2 >= 60:
    hour = mins2 // 60
    minutes = mins2 % 60
    print("Late")
    print(f"{hour}:{minutes:02d} hours after the start")
    