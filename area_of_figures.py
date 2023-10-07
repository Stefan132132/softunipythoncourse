import math

type_figure = input()
area = float()

if type_figure == "square":
    side = float(input())
    area = side * side
    print(area)
elif type_figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
    print(area)
elif type_figure == "circle":
    r = float(input())
    area = math.pi * pow(r, 2)
    format_area = "{:.3f}".format(area)
    print(format_area)
else:
    a = float(input())
    ha = float(input())
    area = (a * ha) / 2
    print(area)