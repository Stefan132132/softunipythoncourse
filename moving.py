width = int(input())
length = int(input())
height = int(input())
total_space = width * length * height
total_space_left = total_space
command = input()

while command != "Done":
    current_boxes = int(command)
    total_space_left -= current_boxes
    if total_space_left <= 0:
        break
    command = input()
    
if command == "Done":
    print(f"{total_space_left} Cubic meters left.")
else:
    space_needed = -total_space_left
    print(f"No more free space! You need {space_needed} Cubic meters more.")