budget = float(input())
number_of_statists = int(input())
statist_clothes_price = float(input())

decor_price = budget * 0.10

statist_clothes_budget = number_of_statists * statist_clothes_price

if number_of_statists > 150:
    statist_clothes_budget = statist_clothes_budget * 0.90

if decor_price + statist_clothes_budget <= budget:
    print("Action!")
    print(f"Wingard starts filming with {budget - (decor_price + statist_clothes_budget):.2f} leva left.")

else:
    print("Not enough money!")
    print(f"Wingard needs {(decor_price + statist_clothes_budget) - budget:.2f} leva more.")












