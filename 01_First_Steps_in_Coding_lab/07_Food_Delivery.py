chicken_meal = int(input())
fish_meal = int(input())
vegan_meal = int(input())

chicken_meal_price = 10.35
fish_meal_price = 12.40
vegan_meal_price = 8.15

delivery_price = 2.50

chicken_order = chicken_meal * chicken_meal_price
fish_order = fish_meal * fish_meal_price
vegan_order = vegan_meal * vegan_meal_price

food_orders_price = chicken_order + fish_order + vegan_order

desert_price = food_orders_price * 0.2

total_price = food_orders_price + desert_price + delivery_price

print(total_price)