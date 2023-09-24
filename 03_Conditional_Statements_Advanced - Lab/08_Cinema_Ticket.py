MONDAY_PRICE = 12
TUESDAY_PRICE = 12
WEDNESDAY_PRICE = 14
THURSDAY_PRICE = 14
FRIDAY_PRICE = 12
SATURDAY_PRICE = 16
SUNDAY_PRICE = 16

day = input()
price = 0

if day == "Monday":
    price = MONDAY_PRICE
elif day == "Tuesday":
    price = TUESDAY_PRICE
elif day == "Wednesday":
    price = WEDNESDAY_PRICE
elif day == "Thursday":
    price = THURSDAY_PRICE
elif day == "Friday":
    price = FRIDAY_PRICE
elif day == "Saturday":
    price = SATURDAY_PRICE
elif day == "Sunday":
    price = SUNDAY_PRICE
print(price)

