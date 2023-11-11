proccessor_price = float(input()) * 1.57
GPU_price = float(input()) * 1.57
RAM_price_per_one = float(input()) * 1.57
quantity_RAM = int(input())
discount_procent = float(input())

proccessor_price_discount = proccessor_price - (proccessor_price * discount_procent)
GPU_price_discount = GPU_price - (GPU_price * discount_procent)

money_needed = proccessor_price_discount + GPU_price_discount + RAM_price_per_one * quantity_RAM
print(f"Money needed - {money_needed:.2f} leva.")

