vacation_price = float(input())
number_of_puzzels = int(input())
number_of_dolls = int(input())
number_of_teddy_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

puzzel_price = 2.60
doll_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2

total_number_of_toys = number_of_puzzels + number_of_dolls + number_of_teddy_bears + \
                       number_of_minions + number_of_trucks

discount = 0
if total_number_of_toys >= 50:
    discount = 0.25

total_price = number_of_puzzels * puzzel_price + number_of_dolls * doll_price + \
              number_of_teddy_bears * teddy_bear_price + number_of_minions * minion_price + \
              number_of_trucks * truck_price

new_total_price = total_price * (1 - discount)
rent = new_total_price * 0.10
profit = new_total_price - rent

if profit >= vacation_price:
    print(f"Yes! {profit - vacation_price:.2f} lv left.")
else:
    print(f"Not enough money! {vacation_price - profit:.2f} lv needed.")
