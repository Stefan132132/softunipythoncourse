not_good_grades = int(input())
failed_times = 0
grade_sum = 0
last_problem = ""
solved_problems_counter = 0
has_failed = True

while failed_times < not_good_grades:
    problem = input()
    if problem == "Enough":
        has_failed = False
        break
    grade = int(input())
    if grade <= 4:
        failed_times += 1
    grade_sum += grade
    solved_problems_counter += 1
    last_problem = problem

if has_failed:
    print(f"You need a break, {not_good_grades} poor grades.")
else:
    print(f"Average score: {(grade_sum / solved_problems_counter):.2f}")
    print(f"Number of problems: {solved_problems_counter}")
    print(f"Last problem: {last_problem}")