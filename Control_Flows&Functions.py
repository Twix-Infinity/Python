price = float(input("Enter the price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

if price < 0 or discount_percent > 100 or price == 0 or discount_percent < 0:
    print("Invalid input. Please enter a valid price above 0 or a discount percentage between 0-100.")

discount_percent = (discount_percent / 100)
discount = (100- discount_percent)

if discount_percent >=0.20:
    final_price = price * discount
else:
    final_price = price

print("The final price after discount is: $", final_price)