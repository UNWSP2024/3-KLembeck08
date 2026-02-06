# Author: Kael Lembeck
# Date: 2/6/2026
# Program Title: Hot Dog Order Calculator

print("Choose a hot dog type:")
print("1. Hot Dog ($3.50)")
print("2. Chili Dog ($4.50)")

choice = int(input("Enter 1 or 2: "))

if choice == 1:
    base_price = 3.50
elif choice == 2:
    base_price = 4.50
else:
    print("Invalid choice.")
    exit()

# Toppings
cheese = input("Add cheese for $0.50 (y/n): ").lower()
peppers = input("Add peppers for $0.75 (y/n): ").lower()
onions = input("Add grilled onions for $1.00 (y/n): ").lower()

topping_total = 0

if cheese == "y":
    topping_total += 0.50
if peppers == "y":
    topping_total += 0.75
if onions == "y":
    topping_total += 1.00

subtotal = base_price + topping_total
tax = subtotal * 0.07
total = subtotal + tax

print(f"Hot dog cost: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total cost: ${total:.2f}")
