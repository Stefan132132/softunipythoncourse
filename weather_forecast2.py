weather_grad = float(input())

if weather_grad >= 5.00 and weather_grad <= 11.9:
    print("Cold")
elif weather_grad >= 12.00 and weather_grad <= 14.9:
    print("Cool")
elif weather_grad >= 15.00 and weather_grad <= 20.00:
    print("Mild")
elif weather_grad >= 20.1 and weather_grad <= 25.9:
    print("Warm")
elif weather_grad >= 26.00 and weather_grad <= 35.00:
    print("Hot")
else:
    print("unknown")