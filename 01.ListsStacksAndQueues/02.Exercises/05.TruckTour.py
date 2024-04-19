from collections import deque

petrol_pumps = int(input())

pump = deque()
for i in range(petrol_pumps):
    pump += deque([input().split(" ")])
for i1 in range(petrol_pumps):
    is_valid = True
    fuel = 0
    for _ in range(petrol_pumps):
        current = pump.popleft()
        fuel += int(current[0]) - int(current[1])
        if fuel < 0:
            is_valid = False
        pump.append(current)
    if is_valid:
        print(i1)
        break
    pump.append(pump.popleft())
