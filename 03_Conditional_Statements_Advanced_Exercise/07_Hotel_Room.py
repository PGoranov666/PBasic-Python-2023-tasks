# MAY_OCTOBER_STUDIO = 50
# MAY_OCTOBER_APARTMENT = 65
# JUNE_SEPTEMBER_STUDIO = 75.20
# JUNE_SEPTEMBER_APARTMENT = 68.70
# JULY_AUGUST_STUDIO = 76
# JULY_AUGUST_APARTMENT = 77
# DISCOUNT_7_MAY_OCTOBER_STUDIO = 0.95
# DISCOUNT_14_MAY_OCTOBER_STUDIO = 0.70
# DISCOUNT_14_JUNE_SEPTEMBER_STUDIO = 0.80
# DISCOUNT_APARTMENT_14 = 0.9
# •	За студио, при повече от 7 нощувки през май и октомври : 5% намаление.
# •	За студио, при повече от 14 нощувки през май и октомври : 30% намаление.
# •	За студио, при повече от 14 нощувки през юни и септември: 20% намаление.
# •	За апартамент, при повече от 14 нощувки, без значение от месеца : 10% намаление.

month = input()
nights = int(input())
studio_price = 0
apartment_price = 0

if month == "May" or month == "October":
    studio_price = 50
    apartment_price = 65
    if nights > 14:
        studio_price *= 0.70
        apartment_price *= 0.90
    elif nights > 7:
        studio_price *= 0.95

elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    if nights > 14:
        studio_price *= 0.80
        apartment_price *= 0.90

elif month == "July" or month == "August":
    studio_price = 76
    apartment_price = 77
    if nights > 14:
        apartment_price *= 0.90

total_studio_price = nights * studio_price
total_apartment_price = nights * apartment_price

print(f"Apartment: {total_apartment_price:.2f} lv.")
print(f"Studio: {total_studio_price:.2f} lv.")
