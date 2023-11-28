item_prices = [100, 30, 150, 45]
item_quantities = [3, 2, 4, 1]
discount_rate = 10
tax_rate = 8       
subtotal = sum(price * quantity for price, quantity in zip(item_prices, item_quantities))
discount_amount = (discount_rate / 100) * subtotal
subtotal_after_discount = subtotal - discount_amount
tax_amount = (tax_rate / 100) * subtotal_after_discount
total_cost = subtotal_after_discount + tax_amount
print(f"Subtotal: {subtotal:.2f}")
print(f"Discount: {discount_amount:.2f}")
print(f"Subtotal after discount: {subtotal_after_discount:.2f}")
print(f"Tax: {tax_amount:.2f}")
print(f"Total Cost: {total_cost:.2f}")
