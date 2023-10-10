fuel = input()
liters = float(input())
club_card = input()

price_gasoline = liters * 2.22
price_diesel = liters * 2.33
price_gas = liters * 0.93

if club_card == "Yes":
    if fuel == "Gasoline":
        discount_price_gasoline = price_gasoline - (0.18 * liters)
    elif fuel == "Diesel":
        discount_price_diesel = price_diesel - (0.12 * liters)
    elif fuel == "Gas":
        discount_price_gas = price_gas - (0.08 * liters)
    
    if liters > 25:
        if fuel == "Gasoline":
            discount = 0.10 * discount_price_gasoline
            discount_price_gasoline = discount_price_gasoline - discount
            print(f"{discount_price_gasoline:.2f} lv.")
        elif fuel == "Diesel":
            discount2 = 0.10 * discount_price_diesel
            discount_price_diesel = discount_price_diesel - discount2
            print(f"{discount_price_diesel:.2f} lv.")
        elif fuel == "Gas":
            discount3 = discount_price_gas * 0.10
            discount_price_gas = discount_price_gas - discount3
            print(f"{discount_price_gas:.2f} lv.")
    elif liters >= 20 and liters <= 25:
        if fuel == "Gasoline":
            discount = 0.08 * discount_price_gasoline
            discount_price_gasoline = discount_price_gasoline - discount
            print(f"{discount_price_gasoline:.2f} lv.")
        elif fuel == "Diesel":
            discount2 = 0.08 * discount_price_diesel
            discount_price_diesel = discount_price_diesel - discount2
            print(f"{discount_price_diesel:.2f} lv.")
        elif fuel == "Gas":
            discount3 = discount_price_gas * 0.08
            discount_price_gas = discount_price_gas - discount3
            print(f"{discount_price_gas:.2f} lv.")
    else:
        if fuel == "Gasoline":
            print(f"{discount_price_gasoline:.2f} lv.")
        elif fuel == "Diesel":
            print(f"{discount_price_diesel:.2f} lv.")
        elif fuel == "Gas":
            print(f"{discount_price_gas:.2f} lv.")
elif club_card == "No":
    if liters > 25:
        if fuel == "Gasoline":
            discount = 0.10 * price_gasoline
            discount_price_gasoline = price_gasoline - discount
            print(f"{discount_price_gasoline:.2f} lv.")
        elif fuel == "Diesel":
            discount2 = 0.10 * price_diesel
            discount_price_diesel = price_diesel - discount2
            print(f"{discount_price_diesel:.2f} lv.")
        elif fuel == "Gas":
            discount3 = price_gas * 0.10
            discount_price_gas = price_gas - discount3
            print(f"{discount_price_gas:.2f} lv.")
    elif liters >= 20 and liters <= 25:
        if fuel == "Gasoline":
            discount = 0.08 * price_gasoline
            discount_price_gasoline = price_gasoline - discount
            print(f"{discount_price_gasoline:.2f} lv.")
        elif fuel == "Diesel":
            discount2 = 0.08 * price_diesel
            discount_price_diesel = price_diesel - discount2
            print(f"{discount_price_diesel:.2f} lv.")
        elif fuel == "Gas":
            discount3 = price_gas * 0.08
            discount_price_gas = price_gas - discount3
            print(f"{discount_price_gas:.2f} lv.")
    else:
        if fuel == "Gasoline":
            print(f"{price_gasoline:.2f} lv.")
        elif fuel == "Diesel":
            print(f"{price_diesel:.2f} lv.")
        elif fuel == "Gas":
            print(f"{price_gas:.2f} lv.")
            
    



