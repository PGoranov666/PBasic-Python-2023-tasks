nylon = int(input())
paint = int(input())
thinner = int(input())
working_hours = int(input())
extra_nylon = nylon + 2
extra_paint = (paint * 0.1) + paint

nylon_price = 1.50
paint_price = 14.50
thinner_price = 5.00

nylon_sum =  extra_nylon * nylon_price
paint_sum = extra_paint * paint_price
thinner_sum = thinner * 5.00
bags_sum = 0.40
materials_sum = nylon_sum + paint_sum + thinner_sum + bags_sum

laborer_per_hour = (materials_sum * 0.3)
laborer_total = laborer_per_hour * working_hours

total_amount = materials_sum + laborer_total

print(float(total_amount))

