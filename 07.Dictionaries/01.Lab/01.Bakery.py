stock = input().split(" ")

result = {stock[i]: int(stock[i + 1]) for i in range(0, len(stock), 2)}

food = input().split(" ")
bakery = {}
for i in range(0, len(stock), 2):
    key = stock[i]
    value = stock[i + 1]
    bakery[key] = int(value)

for i1 in food:
    if i1 in bakery:
        print(f"We have {bakery[i1]} of {i1} left")
    else:
        print(f"Sorry, we don't have {i1}")
        