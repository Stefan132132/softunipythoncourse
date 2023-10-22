n = int(input())
salary = float(input())
sanction = 0

for i in range(0, n):
    website = input()
    if website == "Facebook":
        sanction += 150
    elif website == "Instagram":
        sanction += 100
    elif website == "Reddit":
        sanction += 50
    else:
        continue

if salary <= sanction:
    print("You have lost your salary.")
elif salary > sanction:
    salary_left = salary - sanction
    print(f"{salary_left:.0f}")