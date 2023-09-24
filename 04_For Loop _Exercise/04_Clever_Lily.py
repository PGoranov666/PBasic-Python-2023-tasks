age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

money_amount = 0

for birthdays in range (1, age + 1):
    if birthdays % 2 == 0:
        money_amount += birthdays * 5
        money_amount -= 1
    else:
        money_amount += toy_price

if money_amount >= washing_machine_price:
    print(f"Yes! {money_amount - washing_machine_price :.2f}")
else:
    print(f"No! {washing_machine_price - money_amount :.2f}")

