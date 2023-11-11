money_daily = float(input()) * 5
earned_per_day = float(input()) * 5
costs = float(input())
gift_price = float(input())


money_saved = (money_daily + earned_per_day) - costs

if money_saved >= gift_price:
    print(f"Profit: {money_saved:.2f} BGN, the gift has been purchased.")
elif money_saved < gift_price:
    money_needed = gift_price - money_saved
    print(f"Insufficient money: {money_needed:.2f} BGN.")