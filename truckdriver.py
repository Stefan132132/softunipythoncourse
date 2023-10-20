season = input()
kilometres = float(input())

if season == "Autumn" or season == "Spring":
    if kilometres <= 5000:
        salary = (kilometres * 0.75 * 4) - 0.10 * (kilometres * 0.75 * 4)
        print(f"{salary:.2f}")
    elif 5000 < kilometres <= 10000:
        salary = (kilometres * 0.95 * 4) - 0.10 * (kilometres * 0.95 * 4)
        print(f"{salary:.2f}")
    elif 10000 < kilometres <= 20000:
        salary = (kilometres * 1.45 * 4) - 0.10 * (kilometres * 1.45 * 4)
        print(f"{salary:.2f}")
elif season == "Summer":
    if kilometres <= 5000:
        salary = (kilometres * 0.90 * 4) - 0.10 * (kilometres * 0.90 * 4)
        print(f"{salary:.2f}")
    elif 5000 < kilometres <= 10000:
        salary = (kilometres * 1.10 * 4) - 0.10 * (kilometres * 1.10 * 4)
        print(f"{salary:.2f}")
    elif 10000 < kilometres <= 20000:
        salary = (kilometres * 1.45 * 4) - 0.10 * (kilometres * 1.45 * 4)
        print(f"{salary:.2f}")
elif season == "Winter":
    if kilometres <= 5000:
        salary = (kilometres * 1.05 * 4) - 0.10 * (kilometres * 1.05 * 4)
        print(f"{salary:.2f}")
    elif 5000 < kilometres <= 10000:
        salary = (kilometres * 1.25 * 4) - 0.10 * (kilometres * 1.25 * 4)
        print(f"{salary:.2f}")
    elif 10000 < kilometres <= 20000:
        salary = (kilometres * 1.45 * 4) - 0.10 * (kilometres * 1.45 * 4)
        print(f"{salary:.2f}")