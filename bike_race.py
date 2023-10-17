juniors = int(input())
seniors = int(input())
race_type = input()

if race_type == "trail":
    price_juniors = juniors * 5.50
    price_seniors = seniors * 7
    costs = 0.05 * (price_juniors + price_seniors)
    price = (price_juniors + price_seniors) - costs
    print(f"{price:.2f}")
elif race_type == "cross-country":
    price_juniors = juniors * 8
    price_seniors = seniors * 9.50
    if seniors + juniors >= 50:
        price_juniors = price_juniors - 0.25 * price_juniors
        price_seniors = price_seniors - 0.25 * price_seniors
        costs = 0.05 * (price_juniors + price_seniors)
        price = (price_juniors + price_seniors) - costs
        print(f"{price:.2f}")
    else:
        costs = 0.05 * (price_juniors + price_seniors)
        price = (price_juniors + price_seniors) - costs
        print(f"{price:.2f}")
        
elif race_type == "downhill":
    price_juniors = juniors * 12.25
    price_seniors = seniors * 13.75
    costs = 0.05 * (price_juniors + price_seniors)
    price = (price_juniors + price_seniors) - costs
    print(f"{price:.2f}")
elif race_type == "road":
    price_juniors = juniors * 20
    price_seniors = seniors * 21.50
    costs = 0.05 * (price_juniors + price_seniors)
    price = (price_juniors + price_seniors) - costs
    print(f"{price:.2f}")