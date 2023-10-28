increase = input()
total = 0
while (increase != "NoMoreMoney"):
    if float(increase) < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {float(increase):.2f}")
    total = total + float(increase)
    increase = input()
print(f"Total: {total:.2f}")