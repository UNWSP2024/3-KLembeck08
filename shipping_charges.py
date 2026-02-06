# Author: Kael Lembeck
# Date: 2/6/2026
# Program Title: Shipping Charges

weight = float(input("Enter the package weight in pounds: "))

if weight <= 2:
    rate = 1.50
elif weight <= 6:
    rate = 3.00
elif weight <= 10:
    rate = 4.00
else:
    rate = 4.75

shipping_cost = weight * rate

print(f"The shipping cost is: ${shipping_cost:.2f}")
