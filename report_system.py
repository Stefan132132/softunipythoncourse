needed_charity_sum = int(input())
command_product_price = input()
isGoalReached = False
cash_quantity = 0
cards_quantity = 0
cash_sum = 0
cards_sum = 0
counter_payment = 0
sum_charity = 0

while command_product_price != "End":
    product_price = int(command_product_price)
    if counter_payment % 2 == 0:
        if product_price > 100:
            print("Error in transaction!")
            counter_payment += 1
        else:
            cash_quantity += 1
            cash_sum += product_price
            sum_charity += product_price
            counter_payment += 1
            print("Product sold!")
        if sum_charity >= needed_charity_sum:
            isGoalReached = True
            break
        command_product_price = input()
        continue
    if product_price < 10:
        print("Error in transaction!")
        counter_payment += 1
    else:
        cards_quantity += 1
        cards_sum += product_price
        sum_charity += product_price
        counter_payment += 1
        print("Product sold!")
    if sum_charity >= needed_charity_sum:
            isGoalReached = True
            break
    command_product_price = input()
    
    
if isGoalReached:
    average_cs = cash_sum / cash_quantity
    average_cc = cards_sum / cards_quantity
    print(f"Average CS: {average_cs:.2f}")
    print(f"Average CC: {average_cc:.2f}")
else:
    print("Failed to collect required money for charity.")
            
        