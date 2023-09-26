#Депозирана сума – реално число в интервала [100.00 … 10000.00]
#рок на депозита (в месеци) – цяло число в интервала [1…12]
#Годишен лихвен процент – реално число в интервала [0.00 …100.00]
deposit_amount = float(input())
deposit_term = int(input())
annual_interest = float(input())
#Изчисляваме натрупаната лихва: 200 * 0.057 (5.7%) = 11.40 лв.
#Изчисляваме лихвата за 1 месец: 11.40 лв. / 12 месеца = 0.95 лв.
#Общата сума е: 200 лв. + 3 * 0.95 лв. = 202.85 лв.
interest_per_anum = deposit_amount * annual_interest / 100
interest_per_month = interest_per_anum / 12

print(float(deposit_amount + (deposit_term * interest_per_month)))


