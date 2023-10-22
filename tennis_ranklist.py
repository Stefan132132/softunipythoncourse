import math
tournaments = int(input())
point_given = int(input())
average = 0
count = 0

for _ in range(0, tournaments):
    tournament_progress = input()
    if tournament_progress == "W":
        point_given += 2000
        average += 2000
        count += 1
    elif tournament_progress == "F":
        point_given += 1200
        average += 1200
    elif tournament_progress == "SF":
        point_given += 720
        average += 720
        
average_points = average / tournaments
procent_W = count / tournaments * 100

print(f"Final points: {point_given}")
print(f"Average points: {math.floor(average_points)}")
print(f"{procent_W:.2f}%")