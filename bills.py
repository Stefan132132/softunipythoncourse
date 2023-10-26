months = int(input())
elec = 0
water = 0
internet = 0
other = 0

for i in range(1, months + 1):
    elec_every_month = float(input())
    elec = elec + elec_every_month
    water = water + 20
    internet = internet + 15
    other = other + ((elec_every_month + 20 + 15) + 0.20 *(elec_every_month + 20 + 15))

average = (elec + water + internet + other) / months
print(f"Electricity: {elec:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {average:.2f} lv")