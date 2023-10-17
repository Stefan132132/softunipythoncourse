budget = float(input())
category = input()
people = int(input())

vip = people * 499.99
normal = people * 249.99

if 1 <= people <= 4:
    transport_money = 0.75 * budget
    budget_left = budget - transport_money
    if category == "VIP":
        if budget_left > vip:
            money_left = budget_left - vip
            print(f"Yes! You have {money_left:.2f} leva left.")
        elif vip > budget_left:
            money_needed = vip - budget_left
            print(f"Not enough money! You need {money_needed:.2f} leva.")
    elif category == "Normal":
        if budget_left > normal:
            money_left = budget_left - normal
            print(f"Yes! You have {money_left:.2f} leva left.")
        elif normal > budget_left:
            money_needed = normal - budget_left
            print(f"Not enough money! You need {money_needed:.2f} leva.")
elif 5 <= people <= 9:
    transport_money = 0.60 * budget
    budget_left = budget - transport_money
    if category == "VIP":
        if budget_left > vip:
            money_left = budget_left - vip
            print(f"Yes! You have {money_left:.2f} leva left.")
        elif vip > budget_left:
            money_needed = vip - budget_left
            print(f"Not enough money! You need {money_needed:.2f} leva.")
    elif category == "Normal":
        if budget_left > normal:
            money_left = budget_left - normal
            print(f"Yes! You have {money_left:.2f} leva left.")
        elif normal > budget_left:
            money_needed = normal - budget_left
            print(f"Not enough money! You need {money_needed:.2f} leva.")
elif 10 <= people <= 24:
    transport_money = 0.50 * budget
    budget_left = budget - transport_money
    if category == "VIP":
        if budget_left > vip:
            money_left = budget_left - vip
            print(f"Yes! You have {money_left:.2f} leva left.")
        elif vip > budget_left:
            money_needed = vip - budget_left
            print(f"Not enough money! You need {money_needed:.2f} leva.")
    elif category == "Normal":
        if budget_left > normal:
            money_left = budget_left - normal
            print(f"Yes! You have {money_left:.2f} leva left.")
        elif normal > budget_left:
            money_needed = normal - budget_left
            print(f"Not enough money! You need {money_needed:.2f} leva.")
elif 25 <= people <= 49:
    transport_money = 0.40 * budget
    budget_left = budget - transport_money
    if category == "VIP":
        if budget_left > vip:
            money_left = budget_left - vip
            print(f"Yes! You have {money_left:.2f} leva left.")
        elif vip > budget_left:
            money_needed = vip - budget_left
            print(f"Not enough money! You need {money_needed:.2f} leva.")
    elif category == "Normal":
        if budget_left > normal:
            money_left = budget_left - normal
            print(f"Yes! You have {money_left:.2f} leva left.")
        elif normal > budget_left:
            money_needed = normal - budget_left
            print(f"Not enough money! You need {money_needed:.2f} leva.")
elif people >= 50:
    transport_money = 0.25 * budget
    budget_left = budget - transport_money
    if category == "VIP":
        if budget_left > vip:
            money_left = budget_left - vip
            print(f"Yes! You have {money_left:.2f} leva left.")
        elif vip > budget_left:
            money_needed = vip - budget_left
            print(f"Not enough money! You need {money_needed:.2f} leva.")
    elif category == "Normal":
        if budget_left > normal:
            money_left = budget_left - normal
            print(f"Yes! You have {money_left:.2f} leva left.")
        elif normal > budget_left:
            money_needed = normal - budget_left
            print(f"Not enough money! You need {money_needed:.2f} leva.")
