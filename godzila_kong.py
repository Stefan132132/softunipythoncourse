def main():
    film_budget = float(input())
    statics_count = int(input())
    clothes_price_for_one = float(input())

    film_decor = 0.10 * film_budget
    clothes_generalprice = statics_count * clothes_price_for_one

    if statics_count > 150:
        clothes_generalprice = clothes_generalprice - (0.10 * clothes_generalprice)
        general_price = clothes_generalprice + film_decor
        help_function(general_price, film_budget)
    else:
        general_price = clothes_generalprice + film_decor
        help_function(general_price, film_budget)
        
def help_function(general_price, film_budget):
    if general_price > film_budget:
        money_needed = general_price - film_budget
        print("Not enough money!")
        print(f"Wingard needs {money_needed:.2f} leva more.")
    elif general_price <= film_budget:
        money_left = film_budget - general_price
        print("Action!")
        print(f"Wingard starts filming with {money_left:.2f} leva left.")



main()


        