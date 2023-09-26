BANANA_WEEKDAY = 2.50
BANANA_WEEKEND = 2.70
APPLE_WEEKDAY = 1.20
APPLE_WEEKEND = 1.25
ORANGE_WEEKDAY = 0.85
ORANGE_WEEKEND = 0.90
GRAPEFRUIT_WEEKDAY = 1.45
GRAPEFRUIT_WEEKEND = 1.60
KIWI_WEEKDAY = 2.70
KIWI_WEEKEND = 3.00
PINEAPPLE_WEEKDAY = 5.50
PINEAPPLE_WEEKEND = 5.60
GRAPES_WEEKDAY = 3.85
GRAPES_WEEKEND = 4.20

fruit = input()
day_of_the_week = input()
quantity = float(input())

price = 0

if day_of_the_week == "Monday" or day_of_the_week == "Tuesday" or \
        day_of_the_week == "Wednesday" or day_of_the_week == "Thursday" \
        or day_of_the_week == "Friday":
    if fruit == "banana":
        price = quantity * BANANA_WEEKDAY
        print(f"{price:.2f}")
    elif fruit == "apple":
        price = quantity * APPLE_WEEKDAY
        print(f"{price:.2f}")
    elif fruit == "orange":
        price = quantity * ORANGE_WEEKDAY
        print(f"{price:.2f}")
    elif fruit == "grapefruit":
        price = quantity * GRAPES_WEEKDAY
        print(f"{price:.2f}")
    elif fruit == "kiwi":
        price = quantity * KIWI_WEEKDAY
        print(f"{price:.2f}")
    elif fruit == "pineapple":
        price = quantity * PINEAPPLE_WEEKDAY
        print(f"{price:.2f}")
    elif fruit == "grapes":
        price = quantity * GRAPES_WEEKDAY
        print(f"{price:.2f}")
    else:
        print("error")
elif day_of_the_week == "Saturday" or day_of_the_week == "Sunday":
    if fruit == "banana":
        price = quantity * BANANA_WEEKEND
        print(f"{price:.2f}")
    elif fruit == "apple":
        price = quantity * APPLE_WEEKEND
        print(f"{price:.2f}")
    elif fruit == "orange":
        price = quantity * ORANGE_WEEKEND
        print(f"{price:.2f}")
    elif fruit == "grapefruit":
        price = quantity * GRAPEFRUIT_WEEKEND
        print(f"{price:.2f}")
    elif fruit == "kiwi":
        price = quantity * KIWI_WEEKEND
        print(f"{price:.2f}")
    elif fruit == "pineapple":
        price = quantity * PINEAPPLE_WEEKEND
        print(f"{price:.2f}")
    elif fruit == "grapes":
        price = quantity * GRAPES_WEEKEND
        print(f"{price:.2f}")
    else:
        print("error")
else:
    print("error")


#other
# BANANA_WEEKDAY = 2.50
# BANANA_WEEKEND = 2.70
# APPLE_WEEKDAY = 1.20
# APPLE_WEEKEND = 1.25
# ORANGE_WEEKDAY = 0.85
# ORANGE_WEEKEND = 0.90
# GRAPEFRUIT_WEEKDAY = 1.45
# GRAPEFRUIT_WEEKEND = 1.60
# KIWI_WEEKDAY = 2.70
# KIWI_WEEKEND = 3.00
# PINEAPPLE_WEEKDAY = 5.50
# PINEAPPLE_WEEKEND = 5.60
# GRAPES_WEEKDAY = 3.85
# GRAPES_WEEKEND = 4.20
#
# fruit = input()
# day_of_the_week = input()
# quantity = float(input())
#
# price = 0
# total_price = 0
#
# if fruit == "banana":
#     if day_of_the_week == "Monday" or \
#             day_of_the_week == "Tuesday" or \
#             day_of_the_week == "Wednesday" or \
#             day_of_the_week == "Thursday" or \
#             day_of_the_week == "Friday":
#         price = BANANA_WEEKDAY
#         total_price = quantity * price
#         print(f"{total_price:.2f}")
#     elif day_of_the_week == "Saturday" or \
#             day_of_the_week == "Sunday":
#         price = BANANA_WEEKEND
#         total_price = quantity * price
#         print(f"{total_price:.2f}")
#     else:
#         print("error")
# elif fruit == "apple":
#     if day_of_the_week == "Monday" or \
#             day_of_the_week == "Tuesday" or \
#             day_of_the_week == "Wednesday" or \
#             day_of_the_week == "Thursday" or \
#             day_of_the_week == "Friday":
#         price = APPLE_WEEKDAY
#         total_price = quantity * price
#         print(f"{total_price:.2f}")
#     elif day_of_the_week == "Saturday" or \
#             day_of_the_week == "Sunday":
#         price = APPLE_WEEKEND
#         total_price = quantity * price
#         print(f"{total_price:.2f}")
#     else:
#         print("error")
# elif fruit == "orange":
#     if day_of_the_week == "Monday" or \
#             day_of_the_week == "Tuesday" or \
#             day_of_the_week == "Wednesday" or \
#             day_of_the_week == "Thursday" or \
#             day_of_the_week == "Friday":
#         price = ORANGE_WEEKDAY
#         total_price = quantity * price
#         print(f"{total_price:.2f}")
#     elif day_of_the_week == "Saturday" or \
#             day_of_the_week == "Sunday":
#         price = ORANGE_WEEKEND
#         total_price = quantity * price
#         print(f"{total_price:.2f}")
#     else:
#         print("error")
# elif fruit == "grapefruit":
#     if day_of_the_week == "Monday" or \
#             day_of_the_week == "Tuesday" or \
#             day_of_the_week == "Wednesday" or \
#             day_of_the_week == "Thursday" or \
#             day_of_the_week == "Friday":
#         price = GRAPEFRUIT_WEEKDAY
#         total_price = quantity * price
#         print(f"{total_price:.2f}")
#     elif day_of_the_week == "Saturday" or \
#             day_of_the_week == "Sunday":
#         price = GRAPEFRUIT_WEEKEND
#         total_price = quantity * price
#         print(f"{total_price:.2f}")
#     else:
#         print("error")
# elif fruit == "kiwi":
#     if day_of_the_week == "Monday" or \
#             day_of_the_week == "Tuesday" or \
#             day_of_the_week == "Wednesday" or \
#             day_of_the_week == "Thursday" or \
#             day_of_the_week == "Friday":
#         price = KIWI_WEEKDAY
#         total_price = quantity * price
#         print(f"{total_price:.2f}")
#     elif day_of_the_week == "Saturday" or \
#             day_of_the_week == "Sunday":
#         price = KIWI_WEEKEND
#         total_price = quantity * price
#         print(f"{total_price:.2f}")
#     else:
#         print("error")
# elif fruit == "pineapple":
#     if day_of_the_week == "Monday" or \
#             day_of_the_week == "Tuesday" or \
#             day_of_the_week == "Wednesday" or \
#             day_of_the_week == "Thursday" or \
#             day_of_the_week == "Friday":
#         price = PINEAPPLE_WEEKDAY
#         total_price = quantity * price
#         print(f"{total_price:.2f}")
#     elif day_of_the_week == "Saturday" or \
#             day_of_the_week == "Sunday":
#         price = PINEAPPLE_WEEKEND
#         total_price = quantity * price
#         print(f"{total_price:.2f}")
#     else:
#         print("error")
# elif fruit == "grapes":
#     if day_of_the_week == "Monday" or \
#             day_of_the_week == "Tuesday" or \
#             day_of_the_week == "Wednesday" or \
#             day_of_the_week == "Thursday" or \
#             day_of_the_week == "Friday":
#         price = GRAPES_WEEKDAY
#         total_price = quantity * price
#         print(f"{total_price:.2f}")
#     elif day_of_the_week == "Saturday" or \
#             day_of_the_week == "Sunday":
#         price = GRAPES_WEEKEND
#         total_price = quantity * price
#         print(f"{total_price:.2f}")
#     else:
#         print("error")
# else:
#     print("error")
