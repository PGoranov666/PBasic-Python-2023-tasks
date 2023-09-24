days = int(input())
room_type = input()  # "room for one person", "apartment" или "president apartment"
evaluation = input()  # "positive"  или "negative"

price_per_night = 0
total_price = 0

if room_type == "room for one person":
    price_per_night = 18
    total_price = (days - 1) * price_per_night

elif room_type == "apartment":
    price_per_night = 25
    total_price = (days - 1) * price_per_night
    if days < 10:
        total_price *= 0.7
    elif 10 <= days <= 15:
        total_price *= 0.65
    else:
        total_price *= 0.5

elif room_type == "president apartment":
    price_per_night = 35
    total_price = (days - 1) * price_per_night
    if days < 10:
        total_price *= 0.9
    elif 10 <= days <= 15:
        total_price *= 0.85
    else:
        total_price *= 0.80

if evaluation == "positive":
    total_price += total_price * 0.25

elif evaluation == "negative":
    total_price -= total_price * 0.1

print(f"{total_price:.2f}")
