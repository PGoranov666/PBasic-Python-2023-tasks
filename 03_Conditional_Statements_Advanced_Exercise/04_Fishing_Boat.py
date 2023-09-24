SPRING_RENT = 3000
SUMMER_RENT = 4200
AUTUMN_RENT = 4200
WINTER_RENT = 2600
DISCOUNT_1 = 0.10
DISCOUNT_2 = 0.15
DISCOUNT_3 = 0.25
ADITIONAL_DISCOUNT = 0.05

budget = int(input())
season = input()
fishermen = int(input())

discount_price = 0
total_price = 0

if season == "Spring":
    if fishermen <= 6:
        discount_price = SPRING_RENT - (SPRING_RENT * DISCOUNT_1)
        # total_price = discount_price - (discount_price * ADITIONAL_DISCOUNT)
    elif fishermen <= 11:
        discount_price = SPRING_RENT - (SPRING_RENT * DISCOUNT_2)
        # total_price = discount_price - (discount_price * ADITIONAL_DISCOUNT)
    else:
        discount_price = SPRING_RENT - (SPRING_RENT * DISCOUNT_3)
        # total_price = discount_price - (discount_price * ADITIONAL_DISCOUNT)

elif season == "Summer":
    if fishermen <= 6:
        discount_price = SUMMER_RENT - (SUMMER_RENT * DISCOUNT_1)
        # total_price = discount_price - (discount_price * ADITIONAL_DISCOUNT)
    elif fishermen <= 11:
        discount_price = SUMMER_RENT - (SUMMER_RENT * DISCOUNT_2)
        # total_price = discount_price - (discount_price * ADITIONAL_DISCOUNT)
    else:
        discount_price = SUMMER_RENT - (SUMMER_RENT * DISCOUNT_3)
        # total_price = discount_price - (discount_price * ADITIONAL_DISCOUNT)

elif season == "Autumn":
    if fishermen <= 6:
        discount_price = AUTUMN_RENT - (AUTUMN_RENT * DISCOUNT_1)
        # total_price = discount_price
    elif fishermen <= 11:
        discount_price = AUTUMN_RENT - (AUTUMN_RENT * DISCOUNT_2)
        # total_price = discount_price
    else:
        discount_price = AUTUMN_RENT - (AUTUMN_RENT * DISCOUNT_3)
        # total_price = discount_price

elif season == "Winter":
    if fishermen <= 6:
        discount_price = WINTER_RENT - (WINTER_RENT * DISCOUNT_1)
        # total_price = discount_price - (discount_price * ADITIONAL_DISCOUNT)
    elif fishermen <= 11:
        discount_price = WINTER_RENT - (WINTER_RENT * DISCOUNT_2)
        # total_price = discount_price - (discount_price * ADITIONAL_DISCOUNT)
    else:
        discount_price = WINTER_RENT - (WINTER_RENT * DISCOUNT_3)
        # total_price = discount_price - (discount_price * ADITIONAL_DISCOUNT)

if (season == "Spring" or season == "Summer" or season == "Winter") and \
        (fishermen % 2 == 0):
    total_price = discount_price - (discount_price * ADITIONAL_DISCOUNT)
else:
    total_price = discount_price

if budget >= total_price:
    money_left = budget - total_price
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    needed_money = total_price - budget
    print(f"Not enough money! You need {needed_money:.2f} leva.")
