ticket = input()
rows = int(input())
columns = int(input())

cinema_capacity = rows * columns

if ticket == "Premiere":
    income = cinema_capacity * 12.00
elif ticket == "Normal":
    income = cinema_capacity * 7.50
elif ticket == "Discount":
    income = cinema_capacity * 5.00
    
print(f"{income:.2f} leva")