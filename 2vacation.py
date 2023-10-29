excoursion_money = float(input())
money_inhold = float(input())
day_counter = 0
spent_day_counter = 0
can_save = False

while spent_day_counter < 5:
    spent_or_save = input()
    money = float(input())
    day_counter += 1
    if spent_or_save == "save":
        spent_day_counter = 0
        money_inhold = money_inhold + money
        if money_inhold >= excoursion_money:
            can_save = True
            break
    elif spent_or_save == "spend":
        spent_day_counter += 1
        if money >= money_inhold:
            money_inhold = 0
        else:
            money_inhold = money_inhold - money
        
if can_save:
    print(f"You saved the money for {day_counter} days.")
else:
    print(f"You can't save the money.")
    print(f"{day_counter}")
    
