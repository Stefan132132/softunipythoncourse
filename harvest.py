import math
loze = int(input())
grapes_1km2 = float(input())
wine_needed = int(input())
workers = int(input())

grapes_general = loze * grapes_1km2
wine_liters = (0.40 * grapes_general) / 2.5
wine_left = wine_liters -  wine_needed
wine_for_workers = wine_left / workers

if wine_liters >= wine_needed:
    print(f"Good harvest this year! Total wine: {math.floor(wine_liters)} liters.")
    print(f"{abs(math.ceil(wine_left))} liters left -> {math.ceil(wine_for_workers)} liters per person.")
elif(wine_needed > wine_liters):
    wine_notenough = wine_needed - wine_liters
    print(f"It will be a tough winter! More {math.floor(wine_notenough)} liters wine needed.")