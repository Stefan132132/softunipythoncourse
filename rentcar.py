budget = float(input())
season = input()

car_type = ""
car_class = ""

if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        car_type = "Cabrio"
        car_price = 0.35 * budget
        print(car_class)
        print(f"{car_type} - {car_price:.2f}")
    elif season == "Winter":
        car_type = "Jeep"
        car_price = 0.65 * budget
        print(car_class)
        print(f"{car_type} - {car_price:.2f}")
elif budget > 100 and budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        car_type = "Cabrio"
        car_price = 0.45 * budget
        print(car_class)
        print(f"{car_type} - {car_price:.2f}")
    elif season == "Winter":
        car_type = "Jeep"
        car_price = 0.80 * budget
        print(car_class)
        print(f"{car_type} - {car_price:.2f}")
elif budget > 500:
    car_class = "Luxury class"
    car_type = "Jeep"
    car_price = 0.90 * budget
    print(car_class)
    print(f"{car_type} - {car_price:.2f}")
    