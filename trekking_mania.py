groups = int(input())
group1 = 0
group2 = 0
group3 = 0
group4 = 0
group5 = 0
total_people = 0

for i in range(0, groups):
    people_in_each_group = int(input())
    total_people = total_people + people_in_each_group
    if people_in_each_group <= 5:
        group1 = group1 + people_in_each_group
    elif 6 <= people_in_each_group <= 12:
        group2 = group2 + people_in_each_group
    elif 13 <= people_in_each_group <= 25:
        group3 = group3 + people_in_each_group
    elif 26 <= people_in_each_group <= 40:
        group4 = group4 + people_in_each_group
    elif people_in_each_group >= 41:
        group5 = group5 + people_in_each_group
        

p1 = group1 / total_people * 100
p2 = group2 / total_people * 100
p3 = group3 / total_people * 100
p4 = group4 / total_people * 100
p5 = group5 / total_people * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")


