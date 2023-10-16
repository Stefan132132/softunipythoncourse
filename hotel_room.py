month = input()
nights = int(input())

if month == "May" or month == "October":
    if nights > 14:
        discount_studio = 50 - (0.30 * 50)
        discount_apartament = 65 - (0.10 * 65)
        price_studio = nights * discount_studio
        price_apartament = nights * discount_apartament
        print(f"Apartment: {price_apartament:.2f} lv.")
        print(f"Studio: {price_studio:.2f} lv.")
    elif nights > 7:
        discount_studio = 50 - (0.05 * 50)
        price_studio = nights * discount_studio
        price_apartament = nights * 65
        print(f"Apartment: {price_apartament:.2f} lv.")
        print(f"Studio: {price_studio:.2f} lv.")
    else:
        price_studio = nights * 50
        price_apartament = nights * 65
        print(f"Apartment: {price_apartament:.2f} lv.")
        print(f"Studio: {price_studio:.2f} lv.")
elif month == "June" or month == "September":
    if nights > 14:
        discount_studio = 75.20 - (0.20 * 75.20)
        discount_apartament = 68.70 - (0.10 * 68.70)
        price_studio = nights * discount_studio
        price_apartament = nights * discount_apartament
        print(f"Apartment: {price_apartament:.2f} lv.")
        print(f"Studio: {price_studio:.2f} lv.")
    else:
        price_studio = nights * 75.20
        price_apartament = nights * 68.70
        print(f"Apartment: {price_apartament:.2f} lv.")
        print(f"Studio: {price_studio:.2f} lv.")
elif month == "July" or month == "August":
    if nights > 14:
        discount_apartament = 77 - (0.10 * 77)
        price_studio = nights * 76
        price_apartament = nights * discount_apartament
        print(f"Apartment: {price_apartament:.2f} lv.")
        print(f"Studio: {price_studio:.2f} lv.")
    else:
        price_studio = nights * 76
        price_apartament = nights * 77
        print(f"Apartment: {price_apartament:.2f} lv.")
        print(f"Studio: {price_studio:.2f} lv.")
        