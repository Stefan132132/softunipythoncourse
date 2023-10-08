import math
price_trip = float(input())
puzzle_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

total_count = puzzle_count + dolls_count + bears_count + minions_count + trucks_count
total_price_toys = (puzzle_count * 2.60) + (dolls_count * 3) + (bears_count * 4.10) + (minions_count * 8.20) + (trucks_count * 2)


if total_count >= 50:
    total_price_toys = total_price_toys - (0.25 * total_price_toys)
    total_price_toys = total_price_toys - (0.10 * total_price_toys)
    if total_price_toys >= price_trip:
        money_left = total_price_toys - price_trip
        print(f"Yes! {money_left:.2f} lv left.")
    elif total_price_toys < price_trip:
        money_left = price_trip - total_price_toys
        print(f"Not enough money! {abs(money_left):.2f} lv needed.")
else:
    total_price_toys = total_price_toys - (0.10 * total_price_toys)
    if total_price_toys >= price_trip:
        money_left = total_price_toys - price_trip
        print(f"Yes! {money_left:.2f} lv left.")
    elif total_price_toys < price_trip:
        money_left = price_trip - total_price_toys
        print(f"Not enough money! {abs(money_left):.2f} lv needed.")
