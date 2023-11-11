command_player_name = input()
most_goals = 0

while command_player_name != "END":
    goals = int(input())
    if goals > most_goals:
        most_goals = goals
        best_player = command_player_name
    if most_goals >= 10:
        break
    command_player_name = input()

print(f"{best_player} is the best player!")
if most_goals >= 3:
    print(f"He has scored {most_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {most_goals} goals.")
    