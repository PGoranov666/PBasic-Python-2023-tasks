groups = int(input())

mussala = 0
mont_blanc = 0
kilimanjaro = 0
k2 = 0
everest = 0
for i in range(groups):
    people_in_group = int(input())
    if people_in_group <= 5:
        mussala += people_in_group
    elif people_in_group <= 12:
        mont_blanc += people_in_group
    elif people_in_group <= 25:
        kilimanjaro += people_in_group
    elif people_in_group <= 40:
        k2 += people_in_group
    else:
        everest += people_in_group

people_in_groups = mussala + mont_blanc + kilimanjaro + k2 + everest
musala_percent = mussala / people_in_groups * 100
monblan_percent = mont_blanc / people_in_groups * 100
kilimandjaro_percent = kilimanjaro / people_in_groups * 100
k2_percent = k2 / people_in_groups * 100
everest_percent = everest / people_in_groups * 100

print(f"{musala_percent:.2f}%")
print(f"{monblan_percent:.2f}%")
print(f"{kilimandjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")
