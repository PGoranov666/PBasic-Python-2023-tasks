square_meters = float (input())
price_per_square_meter = float(7.61)
total_price = float(square_meters * price_per_square_meter)
discount = float(total_price * 0.18)
price_with_discount = float(total_price - discount)
#"The final price is: {крайна цена на услугата} lv.""
#"The discount is: {отстъпка} lv."

print(f"The final price is: {price_with_discount} lv.")
print(f"The discount is: {discount} lv.")
