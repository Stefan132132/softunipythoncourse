days = int(input())
room_type = input()
review = input()

nights = days - 1

if room_type == "room for one person":
    price = nights * 18.00
    if review == "positive":
        price = price + (0.25 * price)
        print(f"{price:.2f}")
    elif review == "negative":
        price = price - (0.10 * price)
        print(f"{price:.2f}")
elif room_type == "apartment":
    price = nights * 25
    if days <= 10:
        price = price - (0.30 * price)
        if review == "positive":
            price = price + (0.25 * price)
            print(f"{price:.2f}")
        elif review == "negative":
            price = price - (0.10 * price)
            print(f"{price:.2f}")
    elif 10 < days <= 15:
        price = price - (0.35 * price)
        if review == "positive":
            price = price + (0.25 * price)
            print(f"{price:.2f}")
        elif review == "negative":
            price = price - (0.10 * price)
            print(f"{price:.2f}")
    elif days > 15:
        price = price - (0.50 * price)
        if review == "positive":
            price = price + (0.25 * price)
            print(f"{price:.2f}")
        elif review == "negative":
            price = price - (0.10 * price)
            print(f"{price:.2f}")
elif room_type == "president apartment":
    price = nights * 35
    if days <= 10:
        price = price - (0.10 * price)
        if review == "positive":
            price = price + (0.25 * price)
            print(f"{price:.2f}")
        elif review == "negative":
            price = price - (0.10 * price)
            print(f"{price:.2f}")
    elif 10 < days <= 15:
        price = price - (0.15 * price)
        if review == "positive":
            price = price + (0.25 * price)
            print(f"{price:.2f}")
        elif review == "negative":
            price = price - (0.10 * price)
            print(f"{price:.2f}")
    elif days > 15:
        price = price - (0.20 * price)
        if review == "positive":
            price = price + (0.25 * price)
            print(f"{price:.2f}")
        elif review == "negative":
            price = price - (0.10 * price)
            print(f"{price:.2f}")
        