products = {}
while True:
    stats = input()
    if stats == "statistics":
        break
    stats = stats.split(": ")
    product = stats[0]
    quantity = stats[1]
    if product not in products:
        products[product] = 0

    products[product] += int(quantity)

print("Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")
print(f'Total Products: {len(products.keys())}')
print(f"Total Quantity: {sum(products.values())}")
