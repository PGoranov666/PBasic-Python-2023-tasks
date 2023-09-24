number = int(input())

bonus_points = 0

if number <= 100:
    bonus_points = 5

elif number <= 1000:
    bonus_points = number * 0.20

else:
    bonus_points = number * 0.10

aditional_bonus = 0
if number % 2 == 0:
    aditional_bonus = 1

if number % 10 == 5:
    aditional_bonus = 2

total_bonus = (bonus_points + aditional_bonus)

print(total_bonus)
print(number + total_bonus)
