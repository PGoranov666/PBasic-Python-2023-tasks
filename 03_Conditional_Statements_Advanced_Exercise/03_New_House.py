ROSES_PRICE = 5
DAHLIAS_PRICE = 3.80
TULIPS_PRICE = 2.80
NARCISSUS_PRICE = 3
GLADIOLUS_PRICE = 2.50

flowers_type = input()
flowers_number = int(input())
budget = int(input())

total_price = 0

if flowers_type == "Roses":
    if flowers_number <= 80:
        total_price = flowers_number * ROSES_PRICE
    else:
        total_price = flowers_number * (ROSES_PRICE * 0.90)

elif flowers_type == "Dahlias":
    if flowers_number <= 90:
        total_price = flowers_number * DAHLIAS_PRICE
    else:
        total_price = flowers_number * (DAHLIAS_PRICE * 0.85)

elif flowers_type == "Tulips":
    if flowers_number <= 80:
        total_price = flowers_number * TULIPS_PRICE
    else:
        total_price = flowers_number * (TULIPS_PRICE * 0.85)

elif flowers_type == "Narcissus":
    if flowers_number < 120:
        total_price = flowers_number * (NARCISSUS_PRICE * 1.15)
    else:
        total_price = flowers_number * NARCISSUS_PRICE

elif flowers_type == "Gladiolus":
    if flowers_number < 80:
        total_price = flowers_number * (GLADIOLUS_PRICE * 1.20)
    else:
        total_price = flowers_number * GLADIOLUS_PRICE

if budget >= total_price:
    remaining_amount = budget - total_price
    print(f"Hey, you have a great garden with {flowers_number} {flowers_type} and {remaining_amount:.2f} leva left.")
else:
    needed_amount = total_price - budget
    print(f"Not enough money, you need {needed_amount:.2f} leva more.")
