PREMIERE = 12.00
NORMAL = 7.50
DISCOUNT = 5.00

projection_type = input()
rows = int(input())
columns = int(input())

cinema_capacity = rows * columns

profit = 0

if projection_type == "Premiere":
    profit = cinema_capacity * PREMIERE
    print(f"{profit:.2f} leva")
elif projection_type == "Normal":
    profit = cinema_capacity * NORMAL
    print(f"{profit:.2f} leva")
elif projection_type == "Discount":
    profit = cinema_capacity *DISCOUNT
    print(f"{profit:.2f} leva")
else:
    pass


