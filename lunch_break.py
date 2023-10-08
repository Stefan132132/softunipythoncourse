import math
series = input()
episode_lengh = int(input())
time_break = int(input())

time_lunch_break = 1 / 8 * time_break
time_break_break = 1 / 4 * time_break

time_left =  time_break - (time_lunch_break + time_break_break)

if time_left >= episode_lengh:
    print(f"You have enough time to watch {series} and left with {math.ceil(time_left - episode_lengh)} minutes free time.")
elif time_left < episode_lengh:
    print(f"You don't have enough time to watch {series}, you need {math.ceil(episode_lengh - time_left)} more minutes.")