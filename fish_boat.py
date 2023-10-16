budget = int(input())
season = input()
fishers = int(input())

rent_season_spring = 3000
rent_season_summer_autumn = 4200
rent_season_winter = 2600

money_left = 0
money_needed = 0
discount_rent = 0

if(season == "Spring"):
    if(fishers <= 6):
        discount_rent = rent_season_spring - (rent_season_spring * 0.10)
    elif(7 <= fishers <= 11):
        discount_rent = rent_season_spring - (rent_season_spring * 0.15)
    elif(fishers >= 12):
        discount_rent = rent_season_spring - (rent_season_spring * 0.25)
        
    if fishers % 2 == 0:
        discount_rent = discount_rent - (discount_rent * 0.05)
        if budget >= discount_rent:
            money_left = budget - discount_rent
            print(f"Yes! You have {money_left:.2f} leva left.")
        elif budget < discount_rent:
            money_needed = discount_rent - budget
            print(f"Not enough money! You need {money_needed:.2f} leva.")
    else:
        if budget >= discount_rent:
            money_left = budget - discount_rent
            print(f"Yes! You have {money_left:.2f} leva left.")
        elif budget < discount_rent:
            money_needed = discount_rent - budget
            print(f"Not enough money! You need {money_needed:.2f} leva.")
elif(season == "Summer"):
    if(fishers <= 6):
        discount_rent = rent_season_summer_autumn - (rent_season_summer_autumn * 0.10)
    elif(7 <= fishers <= 11):
        discount_rent = rent_season_summer_autumn - (rent_season_summer_autumn * 0.15)
    elif(fishers >= 12):
        discount_rent = rent_season_summer_autumn - (rent_season_summer_autumn * 0.25)
        
    if fishers % 2 == 0:
        discount_rent = discount_rent - (discount_rent * 0.05)
        if budget >= discount_rent:
            money_left = budget - discount_rent
            print(f"Yes! You have {money_left:.2f} leva left.")
        elif budget < discount_rent:
            money_needed = discount_rent - budget
            print(f"Not enough money! You need {money_needed:.2f} leva.")
    else:
        if budget >= discount_rent:
            money_left = budget - discount_rent
            print(f"Yes! You have {money_left:.2f} leva left.")
        elif budget < discount_rent:
            money_needed = discount_rent - budget
            print(f"Not enough money! You need {money_needed:.2f} leva.")
elif(season == "Autumn"):
    if(fishers <= 6):
        discount_rent = rent_season_summer_autumn - (rent_season_summer_autumn * 0.10)
    elif(7 <= fishers <= 11):
        discount_rent = rent_season_summer_autumn - (rent_season_summer_autumn * 0.15)
    elif(fishers >= 12):
        discount_rent = rent_season_summer_autumn - (rent_season_summer_autumn * 0.25)
        
    if budget >= discount_rent:
            money_left = budget - discount_rent
            print(f"Yes! You have {money_left:.2f} leva left.")
    elif budget < discount_rent:
            money_needed = discount_rent - budget
            print(f"Not enough money! You need {money_needed:.2f} leva.")
elif(season == "Winter"):
    if(fishers <= 6):
        discount_rent = rent_season_winter - (rent_season_winter * 0.10)
    elif(7 <= fishers <= 11):
        discount_rent = rent_season_winter - (rent_season_winter * 0.15)
    elif(fishers >= 12):
        discount_rent = rent_season_winter - (rent_season_winter * 0.25)
        
    if fishers % 2 == 0:
        discount_rent = discount_rent - (discount_rent * 0.05)
        if budget >= discount_rent:
            money_left = budget - discount_rent
            print(f"Yes! You have {money_left:.2f} leva left.")
        elif budget < discount_rent:
            money_needed = discount_rent - budget
            print(f"Not enough money! You need {money_needed:.2f} leva.")
    else:
        if budget >= discount_rent:
            money_left = budget - discount_rent
            print(f"Yes! You have {money_left:.2f} leva left.")
        elif budget < discount_rent:
            money_needed = discount_rent - budget
            print(f"Not enough money! You need {money_needed:.2f} leva.")
        