money_heritage = float(input())
year = int(input())


ivan_years = 19

for i in range(1800, year + 1, 2):
    money_heritage = money_heritage - 12000
for i in range(1801, year + 1, 2):
    money_heritage = money_heritage - (12000 +  50 * ivan_years)
    ivan_years = ivan_years + 2
    
if money_heritage >= 0:
    print(f"Yes! He will live a carefree life and will have {money_heritage:.2f} dollars left.")
elif money_heritage < 0:
    diff = abs(money_heritage)
    print(f"He will need {diff:.2f} dollars to survive.")