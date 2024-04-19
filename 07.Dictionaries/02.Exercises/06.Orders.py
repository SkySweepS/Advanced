order_dict = {}
product_price = {}

while True:
    order = input()
    if order == "buy":
        break
    orders = order.split(" ")
    if orders[0] not in order_dict:
        order_dict[orders[0]] = int(orders[2])
        product_price[orders[0]] = float(orders[1])
    else:
        product_price[orders[0]] = float(orders[1])
        order_dict[orders[0]] += int(orders[2])


for key, value in order_dict.items():
    if key in product_price.keys():
        price = int(value) * product_price[key]
        order_dict[key] = price

for k, v in order_dict.items():
    print(f"{k} -> {v:.2f}")
    