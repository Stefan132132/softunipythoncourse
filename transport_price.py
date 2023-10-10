km = int(input())
time = input()

if km < 20:
    if time == "day":
        money = 0.70 + 0.79 * km
        print(f"{money:.2f}")
    elif time == "night":
        money = 0.70 + 0.90 * km
        print(f"{money:.2f}")
elif km >= 20 and km < 100:
    money = 0.09 * km
    print(f"{money:.2f}")
elif km >= 100:
    money = 0.06 * km
    print(f"{money:.2f}")
