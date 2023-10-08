import math
record_seconds = float(input())
meters_needed_to_swim = float(input())
time_for_a_meter = float(input())

slowed = meters_needed_to_swim / 15
slowed = math.floor(slowed)
new_time = (meters_needed_to_swim * time_for_a_meter) + (slowed * 12.5)
if new_time < record_seconds:
    print(f"Yes, he succeeded! The new world record is {new_time:.2f} seconds.")
else:
    seconds_more = new_time - record_seconds
    print(f"No, he failed! He was {seconds_more:.2f} seconds slower.")
        
        
        




# if meters_needed_to_swim >= 15:
#     slowed = meters_needed_to_swim / 15
#     slowed = math.floor(slowed)
#     new_time = (meters_needed_to_swim * time_for_a_meter) + (slowed * 12.5)
#     if new_time < record_seconds:
#         print(f"Yes, he succeeded! The new world record is {new_time:.2f} seconds.")
#     else:
#         seconds_more = new_time - record_seconds
#         print(f"No, he failed! He was {seconds_more:.2f} seconds slower.")
# else:
#     new_time = meters_needed_to_swim * time_for_a_meter
#     if new_time < record_seconds:
#         print(f"Yes, he succeeded! The new world record is {new_time:.2f} seconds.")
#     else:
#         seconds_more = new_time - record_seconds
#         print(f"No, he failed! He was {seconds_more:.2f} seconds slower.")