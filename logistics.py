cargo_count = int(input())

all_tons = 0
tons1 = 0
tons2 = 0
tons3 = 0
price_1 = 0
price_2 = 0
price_3 = 0
for i in range(1 , cargo_count + 1):
    tons_of_cargo = int(input())
    all_tons = all_tons + tons_of_cargo
    if tons_of_cargo <= 3:
        price_1 = price_1 + (tons_of_cargo * 200)
        tons1 = tons1 + tons_of_cargo
    elif 4 <= tons_of_cargo <= 11:
        price_2 = price_2 + (tons_of_cargo * 175)
        tons2 = tons2 + tons_of_cargo
    elif tons_of_cargo >= 12:
        price_3 = price_3 + (tons_of_cargo * 120)
        tons3 = tons3 + tons_of_cargo

price = (price_1 + price_2 + price_3) / all_tons
procent1 = tons1/all_tons*100
procent2 = tons2/all_tons*100
procent3 = tons3/all_tons*100

print(f"{price:.2f}")
print(f"{procent1:.2f}%")
print(f"{procent2:.2f}%")
print(f"{procent3:.2f}%")
