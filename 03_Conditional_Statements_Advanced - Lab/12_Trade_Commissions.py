SOFIA_1 = 0.05
SOFIA_2 = 0.07
SOFIA_3 = 0.08
SOFIA_4 = 0.12
VARNA_1 = 0.045
VARNA_2 = 0.075
VARNA_3 = 0.10
VARNA_4 = 0.13
PLOVDIV_1 = 0.055
PLOVDIV_2 = 0.08
PLOVDIV_3 = 0.12
PLOVDIV_4 = 0.145

city = input()
sales_volume = float(input())

commission = 0

if city == "Sofia":
    if 0 <= sales_volume <= 500:
        commission = SOFIA_1
    elif 500 < sales_volume <= 1000:
        commission = SOFIA_2
    elif 1000 < sales_volume <= 10000:
        commission = SOFIA_3
    elif sales_volume > 10000:
        commission = SOFIA_4

elif city == "Varna":
    if 0 <= sales_volume <= 500:
        commission = VARNA_1
    elif 500 < sales_volume <= 1000:
        commission = VARNA_2
    elif 1000 < sales_volume <= 10000:
        commission = VARNA_3
    elif sales_volume > 10000:
        commission = VARNA_4

elif city == "Plovdiv":
    if 0 <= sales_volume <= 500:
        commission = PLOVDIV_1
    elif 500 < sales_volume <= 1000:
        commission = PLOVDIV_2
    elif 1000 < sales_volume <= 10000:
        commission = PLOVDIV_3
    elif sales_volume > 10000:
        commission = PLOVDIV_4

if commission == 0:
    print("error")
else:
    income = sales_volume * commission
    print(f"{income:.2f}")
