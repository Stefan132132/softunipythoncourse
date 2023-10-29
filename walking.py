steps = input()
total_steps = 0
goal_reached = False


while True:
    if steps == "Going home":
        steps = int(input())
        total_steps += steps
        if total_steps >= 10000:
            goal_reached = True
            break
        else:
            steps_needed = 10000 - total_steps
            break
    current_steps = int(steps)
    total_steps += current_steps
    if total_steps >= 10000:
        goal_reached = True
        break
    steps = input()
    
    
if goal_reached:
    print(f"Goal reached! Good job!")
    print(f"{total_steps - 10000} steps over the goal!")
else:
    print(f"{steps_needed} more steps to reach goal.")