DESTINATION_1 = "Bulgaria"
DESTINATION_2 = "Balkans"
DESTINATION_3 = "Europe"
ACCOMMODATION_1 = "Camp"
ACCOMMODATION_2 = "Hotel"
SUMMER_LOW_BUDGET = 0.30
SUMMER_HIGH_BUDGET = 0.40
WINTER_LOW_BUDGET = 0.70
WINTER_HIGH_BUDGET = 0.80
BIG_BUDGET = 0.90

budget = float(input())
season = input()
destination = ""
accommodation = ""
price = 0

if budget <= 100:
    destination = DESTINATION_1
    if season == "summer":
        price = budget * SUMMER_LOW_BUDGET
        accommodation = ACCOMMODATION_1
    else:
        price = budget * WINTER_LOW_BUDGET
        accommodation = ACCOMMODATION_2

elif budget <= 1000:
    destination = DESTINATION_2
    if season == "summer":
        price = budget * SUMMER_HIGH_BUDGET
        accommodation = ACCOMMODATION_1
    else:
        price = budget * WINTER_HIGH_BUDGET
        accommodation = ACCOMMODATION_2
else:
    destination = DESTINATION_3
    price = budget * BIG_BUDGET
    accommodation = ACCOMMODATION_2

print(f"Somewhere in {destination}")
print(f"{accommodation} - {price:.2f}")
