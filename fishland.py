mackerel = float(input())
sprinkle = float(input())
bonito_kg = float(input())
safrid_kg = float(input())
mussels_kg = float(input())

bonito_price = (mackerel + (mackerel * 0.60)) * bonito_kg
safrid_price = (sprinkle + (sprinkle * 0.80)) * safrid_kg
mussels_price = mussels_kg * 7.50

print(f"{bonito_price + safrid_price + mussels_price:.2f}")
