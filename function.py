def calculate_discount(price, discount_percent):
    if discount_percent >= 0.2:
        final_price = price - price*discount_percent
    else:
        final_price = price
    return final_price
price_value = input("Enter item price: ")
discount_percent_value = input("Enter discount: ")        
print(calculate_discount(float(price_value), float(discount_percent_value)))
