actor_name = input()
point_academy = float(input())
graders = int(input())

for i in range(0, graders):
    name_grader = input()
    points_grader = float(input())   
    point_academy = point_academy + ((len(name_grader) * points_grader) / 2)
    if point_academy >= 1250.5:
        break

if point_academy < 1250.5:
    points_needed = 1250.5 - point_academy
    print(f"Sorry, {actor_name} you need {points_needed:.1f} more!")
elif point_academy >= 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {point_academy:.1f}!")