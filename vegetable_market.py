veg = float(input())
fruit = float(input())
kg_veg = int(input())
kg_fruit = int(input())

price_lv = (veg * kg_veg) + (fruit * kg_fruit)
price_euro = price_lv / 1.94

print(f"{price_euro:.2f}")