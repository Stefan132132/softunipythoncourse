budget = float(input())
season = input()
destination = ""
vacation_type = ""
money_spent = 0

if budget <= 100:
    if season == "summer":
        money_spent = budget * 0.30
        destination = "Bulgaria"
        vacation_type = "Camp"
        print(f"Somewhere in {destination}")
        print(f"{vacation_type} - {money_spent:.2f}")
    elif season == "winter":
        money_spent = budget * 0.70
        destination = "Bulgaria"
        vacation_type = "Hotel"
        print(f"Somewhere in {destination}")
        print(f"{vacation_type} - {money_spent:.2f}")
elif budget <= 1000:
    if season == "summer":
        money_spent = budget * 0.40
        destination = "Balkans"
        vacation_type = "Camp"
        print(f"Somewhere in {destination}")
        print(f"{vacation_type} - {money_spent:.2f}")
    elif season == "winter":
        money_spent = budget * 0.80
        destination = "Balkans"
        vacation_type = "Hotel"
        print(f"Somewhere in {destination}")
        print(f"{vacation_type} - {money_spent:.2f}")
elif budget > 1000:
    money_spent = budget * 0.90
    destination = "Europe"
    vacation_type = "Hotel"
    print(f"Somewhere in {destination}")
    print(f"{vacation_type} - {money_spent:.2f}")