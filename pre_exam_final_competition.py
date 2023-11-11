dancers_count = int(input())
points = float(input())
season = input()
country = input()

if country == "Bulgaria":
    money = points * dancers_count
    if season == "summer":
        money = money - 0.05 * money
    elif season == "winter":
        money = money - 0.08 * money
elif country == "Abroad":
    money = dancers_count * points + (0.50 * (dancers_count * points))
    if season == "summer":
        money = money - 0.10 * money
    elif season == "winter":
        money = money - 0.15 * money
        
        


charity = 0.75 * money
money_per_dancer = (money - charity) / dancers_count
print(f"Charity - {charity:.2f}")
print(f"Money per dancer - {money_per_dancer:.2f}")