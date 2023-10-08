def main():
    hour = int(input())
    minutes = int(input())

    minutes = minutes + 15

    if minutes >= 60:
        hour = hour + (minutes // 60)
        minutes = minutes % 60
        if hour <= 23:
            check_minutes(hour, minutes)
        elif hour > 23:
            hour = hour % 24
            check_minutes(hour, minutes)
            
    else:
        if hour <= 23:
            check_minutes(hour, minutes)
        elif hour > 23:
            hour = hour % 24
            check_minutes(hour, minutes)
                
def check_minutes(hour, minutes):
    if minutes < 10:
        print(f"{hour}:0{minutes}")
    elif minutes >= 10:
         print(f"{hour}:{minutes}")

main()
    