budget = float(input())
number_videocards = int(input())
number_procesors = int(input())
number_ram = int(input())

videocard_sum = number_videocards * 250
procesor_price = videocard_sum * 0.35
ram_price = videocard_sum * 0.10

total_price = (videocard_sum) + (number_procesors * procesor_price) + (number_ram * ram_price)

if number_videocards > number_procesors:
    total_price *= 0.85

if budget >= total_price:
    print(f"You have {budget - total_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")
