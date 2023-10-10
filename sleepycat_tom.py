vacation_days = int(input())
sleeping_norm = 30000

workday_playtime = (365 - vacation_days) * 63
dayoff_playtime = vacation_days * 127

play_time = workday_playtime + dayoff_playtime

sub = play_time - sleeping_norm
hours = abs(sub) // 60
minutes = abs(sub) % 60
 
if play_time > sleeping_norm:
    print(f"Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
elif sleeping_norm > play_time:
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
    