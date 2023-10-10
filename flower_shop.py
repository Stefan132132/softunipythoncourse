import math
flower1 = int(input())
flower2 = int(input())
flower3 = int(input())
flower4 = int(input())
gift_price = float(input())

money_earned = flower1 * 3.25 + flower2 * 4 + flower3 * 3.50 + flower4 * 8
cost = 0.05 * money_earned
money_earned = money_earned - cost

if money_earned >= gift_price:
    money_left = money_earned - gift_price
    print(f"She is left with {math.floor(money_left)} leva.")
elif money_earned < gift_price:
    money_needed = gift_price - money_earned
    print(f"She will have to borrow {math.ceil(money_needed)} leva.")