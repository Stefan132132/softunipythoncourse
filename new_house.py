flower_type = input()
flower_number = int(input())
budget = int(input())

discount = 0
cost = 0

if flower_type == "Roses":
    if flower_number > 80:
        discount = 0.10
        price = (flower_number * 5) * discount
        cost = (flower_number * 5) - price
    else:
        cost = flower_number * 5
elif flower_type == "Dahlias":
    if flower_number > 90:
        discount = 0.15
        price = (flower_number * 3.80) * discount
        cost = (flower_number * 3.80) - price
    else:
        cost = flower_number * 3.80
elif flower_type == "Tulips":
    if flower_number > 80:
        discount = 0.15
        price = (flower_number * 2.80) * discount
        cost = (flower_number * 2.80) - price
    else:
        cost = flower_number * 2.80
elif flower_type == "Narcissus":
    if flower_number < 120:
        discount = 0.15
        price = (flower_number * 3) * discount
        cost = (flower_number * 3) + price
    else:
        cost = flower_number * 3
elif flower_type == "Gladiolus":
    if flower_number < 80:
        discount = 0.20
        price = (flower_number * 2.50) * discount
        cost = (flower_number * 2.50) + price
    else:
        cost = flower_number * 2.50
        
if cost <= budget:
    money_left = budget - cost
    print(f"Hey, you have a great garden with {flower_number} {flower_type} and {money_left:.2f} leva left.")       
elif cost >= budget:
    money_needed = cost - budget
    print(f"Not enough money, you need {money_needed:.2f} leva more.")
