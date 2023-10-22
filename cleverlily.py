age = int(input())
price_peralnq = float(input())
price_per_toy = int(input())

sum_even = 0
num_toys = 0

for i in range(2, age + 1, 2):
    sum_even += i * 5
for bro in range(2, age + 1, 2):
    sum_even -= 1
for toys in range(1, age + 1, 2):
    num_toys += 1
    
price_from_toys = price_per_toy * num_toys
sum_money = price_from_toys + sum_even

if price_peralnq <= sum_money:
    money_left = sum_money - price_peralnq
    print(f"Yes! {money_left:.2f}")
elif price_peralnq > sum_money:
    money_needed = price_peralnq - sum_money
    print(f"No! {money_needed:.2f}")