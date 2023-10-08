budget = float(input())
graphic_cards = int(input())
processors = int(input())
RAM_memory = int(input())

graphic_cards_price = graphic_cards * 250
processors_price = (0.35 * graphic_cards_price) * processors
RAM_memory_price = (0.10 * graphic_cards_price) * RAM_memory

money_needed = graphic_cards_price + processors_price + RAM_memory_price

if graphic_cards > processors:
    money_needed = money_needed - (0.15 * money_needed)

if budget >= money_needed:
    print(f"You have {(budget - money_needed):.2f} leva left!")
else:
    print(f"Not enough money! You need {(money_needed - budget):.2f} leva more!")