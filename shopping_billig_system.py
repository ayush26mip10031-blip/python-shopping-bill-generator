cart = []
prices = []

print("--- Shopping Billing System ---")
while True:
    item = input("Enter item name (or type 'done' to finish): ")
    if item.lower() == 'done':
        break
    price = float(input(f"Enter price for {item}: "))
    cart.append(item)
    prices.append(price)

print("\n" + "="*25)
print("       RECEIPT       ")
print("="*25)
for i in range(len(cart)):
    print(f"{cart[i]:<15} ₹{prices[i]:.2f}")

subtotal = sum(prices)
tax = subtotal * 0.05  # 5% tax
total = subtotal + tax

print("-" * 25)
print(f"Subtotal:       ₹{subtotal:.2f}")
print(f"Tax (5%):       ₹{tax:.2f}")
print(f"Grand Total:    ₹{total:.2f}")
print("="*25)