frontside_x = float(input())
side_y = float(input())
triangle_height = float(input())

area_front = (frontside_x * frontside_x) - (1.2 * 2)
area_side = (frontside_x * side_y) - (1.5 * 1.5)
area_triangle = (frontside_x * triangle_height) / 2
area_rectangle = frontside_x * side_y

green_paint = (area_front + (area_front + 1.2 * 2)  + (area_side * 2)) / 3.4
red_paint = (area_triangle * 2 + area_rectangle * 2) / 4.3

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")