city = input()
s = float(input())
procent_of = 0

if city == "Sofia":
    if 0 <= s <= 500:
        procent_of = s * 0.05
    elif 500 < s <= 1000:
        procent_of = s * 0.07
    elif 1000 < s <= 10000:
        procent_of = s * 0.08
    elif s > 10000:
        procent_of = s * 0.12
elif city == "Varna":
    if 0 <= s <= 500:
        procent_of = s * 0.045
    elif 500 < s <= 1000:
        procent_of = s * 0.075
    elif 1000 < s <= 10000:
        procent_of = s * 0.10
    elif s > 10000:
        procent_of = s * 0.13
elif city == "Plovdiv":
    if 0 <= s <= 500:
        procent_of = s * 0.055
    elif 500 < s <= 1000:
        procent_of = s * 0.08
    elif 1000 < s <= 10000:
        procent_of = s * 0.12
    elif s > 10000:
        procent_of = s * 0.145
        
        
if procent_of != 0:
    print(f"{procent_of:.2f}")
else:
    print("error")