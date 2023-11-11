days = int(input())
liters_sum = 0
grad_sum = 0
grad_total = 0

for i in range(0, days):
    rakia_liters = float(input())
    grad = float(input())
    liters_sum += rakia_liters
    grad_sum = rakia_liters * grad
    grad_total += grad_sum
    
degrees = grad_total / liters_sum
print(f"Liter: {liters_sum:.2f}")
print(f"Degrees: {degrees:.2f}")
if degrees < 38:
    print("Not good, you should baking!")
elif 38 <= degrees <= 42:
    print("Super!")
elif degrees > 42:
    print("Dilution with distilled water!")
    