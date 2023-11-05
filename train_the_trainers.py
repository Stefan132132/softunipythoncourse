n = int(input())
command_presentation = input()
sum_grade = 0
sum_all_grades = 0
grade_counter = 0

while command_presentation != "Finish":
    for i in range(1, n + 1):
        grade = float(input())
        grade_counter += 1
        sum_grade = sum_grade + grade
    print(f"{command_presentation} - {(sum_grade / n):.2f}.")
    sum_all_grades += sum_grade
    sum_grade = 0
    command_presentation = input()

print(f"Student's final assessment is {(sum_all_grades / grade_counter):.2f}.")
        