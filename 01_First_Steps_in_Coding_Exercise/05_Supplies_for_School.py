pens = int(input())
markers = int(input())
cleaner_detergent = int(input())
discount_percent = int(input())

pens_price = pens * 5.80
markers_price = markers * 7.20
cleaner_detergent_price = cleaner_detergent *  1.20

total_price = pens_price + markers_price + cleaner_detergent_price
discount = discount_percent / 100

final_price = total_price - (total_price * discount)

print(float(final_price))
