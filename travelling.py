command_destination = input()
saved = 0

while command_destination != "End":
    need_money = float(input())
    while saved < need_money:
        saved_money = float(input())
        saved = saved + saved_money
    print(f"Going to {command_destination}!")
    saved = 0
    command_destination = input()
    
    