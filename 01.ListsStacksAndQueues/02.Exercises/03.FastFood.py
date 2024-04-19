from collections import deque

total_food = int(input())
orders = deque([int(x) for x in input().split(" ")])
print(max(orders))
complete = True
while orders:
    current_order = orders.popleft()

    if total_food >= current_order:
        total_food -= current_order
    else:
        complete = False
        orders.appendleft(current_order)
        break

if complete:
    print(f"Orders complete")
else:
    print(f"Orders left: {' '.join([str(x) for x in orders])}")

