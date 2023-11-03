detergent = int(input())
command_dishes_pots = input()
ml_detergent = detergent * 750
isEnough = True
counter = 1
dishes = 0
pots = 0

while command_dishes_pots != "End":
    dishes_pots = int(command_dishes_pots)
    if counter % 3 != 0:
        ml_detergent = ml_detergent - (dishes_pots * 5)
        dishes = dishes + dishes_pots
        counter += 1
        if ml_detergent < 0:
            isEnough = False
            break
        command_dishes_pots = input()
        continue
    ml_detergent = ml_detergent - (dishes_pots * 15)
    pots = pots + dishes_pots
    counter += 1
    if ml_detergent < 0:
        isEnough = False
        break
    command_dishes_pots = input()
    
if isEnough:
    print("Detergent was enough!")
    print(f"{dishes} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {ml_detergent} ml.")
else:
    detergent_needed = -ml_detergent
    print(f"Not enough detergent, {detergent_needed} ml. more necessary!")