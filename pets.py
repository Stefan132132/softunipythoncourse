import math
days = int(input())
food_kg = int(input())
dog_food_kg_daily = float(input())
cat_food_kg_daily = float(input())
turtle_food_grams_daily = float(input())

food_dog = dog_food_kg_daily * days
food_cat = cat_food_kg_daily * days
food_turtle = (turtle_food_grams_daily * days) / 1000
food_needed = food_dog + food_cat + food_turtle

if food_kg >= food_needed:
    food_left = food_kg - food_needed
    print(f"{math.floor(food_left)} kilos of food left.")
elif food_needed > food_kg:
    food_notenough = food_needed - food_kg
    print(f"{math.ceil(food_notenough)} more kilos of food are needed.")
