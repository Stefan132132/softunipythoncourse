h = float(input())
w = float(input())

width_space = ((w * 100) - 100) // 70
height_space = (h * 100) // 120

answer = (width_space * height_space) - 3

print(f"{answer:.0f}")

