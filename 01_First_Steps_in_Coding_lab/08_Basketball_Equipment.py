training_price_per_annum = int(input())

shoes_price = training_price_per_annum - (training_price_per_annum * 0.4)
outfit_price = shoes_price - (shoes_price * 0.2)
ball_price = outfit_price * 0.25
accessories_price = ball_price * 0.2

total_expenses = training_price_per_annum + shoes_price + outfit_price + ball_price + accessories_price

print(total_expenses)

