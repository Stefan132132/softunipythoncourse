students = int(input())

counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
all_grade = 0
for i in range(1, students + 1):
    grade = float(input())
    all_grade = all_grade + grade
    if 2.00 <= grade <= 2.99:
        counter1 += 1
    elif 3.00 <= grade <= 3.99:
        counter2 += 1
    elif 4 <= grade <= 4.99:
        counter3 += 1
    elif grade >= 5.00:
        counter4 += 1

procent1 = counter1/students*100
procent2 = counter2/students*100
procent3 = counter3/students*100
procent4 = counter4/students*100
all_grade = all_grade/students

print(f"Top students: {procent4:.2f}%")
print(f"Between 4.00 and 4.99: {procent3:.2f}%")
print(f"Between 3.00 and 3.99: {procent2:.2f}%")
print(f"Fail: {procent1:.2f}%")
print(f"Average: {all_grade:.2f}")
