# Author: Kael Lembeck
# Date: 2/6/2026
# Program Title: Total Purchase Calculator

item1 = float(input("Enter price of item 1: "))
item2 = float(input("Enter price of item 2: "))
item3 = float(input("Enter price of item 3: "))
item4 = float(input("Enter price of item 4: "))
item5 = float(input("Enter price of item 5: "))

subtotal = item1 + item2 + item3 + item4 + item5
tax = subtotal * 0.07
total = subtotal + tax

print(f"Subtotal: ${subtotal:.2f}")
print(f"Sales Tax (7%): ${tax:.2f}")
print(f"Total: ${total:.2f}")
