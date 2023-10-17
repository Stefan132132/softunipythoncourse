flower1h = int(input())
flower2r = int(input())
flower3l = int(input())
season = input()
holiday = input()

if season == "Spring":
    price_flower1 = 2.00
    price_flower2 = 4.10
    price_flower3 = 2.50
    if holiday == "Y":
        price_flower1 = price_flower1 + 0.15 * price_flower1
        price_flower3 = price_flower3 + 0.15 * price_flower3
        price_flower2 = price_flower2 + 0.15 * price_flower2
        price = price_flower1 * flower1h + price_flower2 * flower2r + price_flower3 * flower3l
        if flower1h + flower2r + flower3l > 20:
            price = (price - 0.20 * price)
        if flower3l > 7:
            price = (price - 0.05 * price)
        print(f"{(2 + price):.2f}")
    elif holiday == "N":
        price = price_flower1 * flower1h + price_flower2 * flower2r + price_flower3 * flower3l
        if flower1h + flower2r + flower3l > 20:
            price = (price - 0.20 * price)
        if flower3l > 7:
            price = (price - 0.05 * price)
        print(f"{(2 + price):.2f}")
elif season == "Summer":
    price_flower1 = 2.00
    price_flower2 = 4.10
    price_flower3 = 2.50
    if holiday == "Y":
        price_flower1 = price_flower1 + 0.15 * price_flower1
        price_flower3 = price_flower3 + 0.15 * price_flower3
        price_flower2 = price_flower2 + 0.15 * price_flower2
        price = price_flower1 * flower1h + price_flower2 * flower2r + price_flower3 * flower3l
        if flower1h + flower2r + flower3l > 20:
            price = (price - 0.20 * price)
        print(f"{(2 + price):.2f}")
    elif holiday == "N":
        price = price_flower1 * flower1h + price_flower2 * flower2r + price_flower3 * flower3l
        if flower1h + flower2r + flower3l > 20:
            price = (price - 0.20 * price)
        print(f"{(2 + price):.2f}")
elif season == "Autumn":
    price_flower1 = 3.75
    price_flower2 = 4.50
    price_flower3 = 4.15
    if holiday == "Y":
        price_flower1 = price_flower1 + 0.15 * price_flower1
        price_flower3 = price_flower3 + 0.15 * price_flower3
        price_flower2 = price_flower2 + 0.15 * price_flower2
        price = price_flower1 * flower1h + price_flower2 * flower2r + price_flower3 * flower3l
        if flower1h + flower2r + flower3l > 20:
            price = (price - 0.20 * price)
        print(f"{(2 + price):.2f}")
    elif holiday == "N":
        price = price_flower1 * flower1h + price_flower2 * flower2r + price_flower3 * flower3l
        if flower1h + flower2r + flower3l > 20:
            price = (price - 0.20 * price)
        print(f"{(2 + price):.2f}")
elif season == "Winter":
    price_flower1 = 3.75
    price_flower2 = 4.50
    price_flower3 = 4.15
    if holiday == "Y":
        price_flower1 = price_flower1 + 0.15 * price_flower1
        price_flower3 = price_flower3 + 0.15 * price_flower3
        price_flower2 = price_flower2 + 0.15 * price_flower2
        price = price_flower1 * flower1h + price_flower2 * flower2r + price_flower3 * flower3l
        if flower1h + flower2r + flower3l > 20:
            price = (price - 0.20 * price) 
        if flower2r >= 10:
            price = (price - 0.10 * price) 
        print(f"{(2 + price):.2f}")
    elif holiday == "N":
        price = price_flower1 * flower1h + price_flower2 * flower2r + price_flower3 * flower3l
        if flower2r >= 10:
            price = (price - 0.10 * price)
        if flower1h + flower2r + flower3l > 20:
            price = (price - 0.20 * price)
        print(f"{(2 + price):.2f}")