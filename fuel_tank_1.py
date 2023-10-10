fuel = input()
liters_in_tank = float(input())
fuel = fuel.lower()

if fuel == "diesel" or fuel == "gas" or fuel == "gasoline":
    if liters_in_tank < 25:
        print(f"Fill your tank with {fuel}!")
    elif liters_in_tank >= 25:
        print(f"You have enough {fuel}.")
else:
    print("Invalid fuel!")
    