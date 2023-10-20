season = input()
group_type = input()
students = int(input())
nights = int(input())

sport_type = ""
price = 0

if season == "Winter":
    if group_type == "boys" or group_type == "girls":
        price = students * 9.60 * nights
        if students >= 50:
            price = price - 0.50 * price
        elif 20 <= students < 50:
            price = price - 0.15 * price
        elif 10 <= students < 20:
            price = price - 0.05 * price
    elif group_type == "mixed":
        price = students * 10 * nights
        if students >= 50:
            price = price - 0.50 * price
        elif 20 <= students < 50:
            price = price - 0.15 * price
        elif 10 <= students < 20:
            price = price - 0.05 * price
elif season == "Spring":
    if group_type == "boys" or group_type == "girls":
        price = students * 7.20 * nights
        if students >= 50:
            price = price - 0.50 * price
        elif 20 <= students < 50:
            price = price - 0.15 * price
        elif 10 <= students < 20:
            price = price - 0.05 * price
    elif group_type == "mixed":
        price = students * 9.50 * nights
        if students >= 50:
            price = price - 0.50 * price
        elif 20 <= students < 50:
            price = price - 0.15 * price
        elif 10 <= students < 20:
            price = price - 0.05 * price
elif season == "Summer":
    if group_type == "boys" or group_type == "girls":
        price = students * 15 * nights
        if students >= 50:
            price = price - 0.50 * price
        elif 20 <= students < 50:
            price = price - 0.15 * price
        elif 10 <= students < 20:
            price = price - 0.05 * price
    elif group_type == "mixed":
        price = students * 20 * nights
        if students >= 50:
            price = price - 0.50 * price
        elif 20 <= students < 50:
            price = price - 0.15 * price
        elif 10 <= students < 20:
            price = price - 0.05 * price
            
if season == "Winter":
    if group_type == "girls":
        sport_type = "Gymnastics"
    elif group_type == "boys":
        sport_type = "Judo"
    elif group_type == "mixed":
        sport_type = "Ski"
elif season == "Spring":
    if group_type == "girls":
        sport_type = "Athletics"
    elif group_type == "boys":
        sport_type = "Tennis"
    elif group_type == "mixed":
        sport_type = "Cycling"
elif season == "Summer":
    if group_type == "girls":
        sport_type = "Volleyball"
    elif group_type == "boys":
        sport_type = "Football"
    elif group_type == "mixed":
        sport_type = "Swimming"
        
print(f"{sport_type} {price:.2f} lv.")