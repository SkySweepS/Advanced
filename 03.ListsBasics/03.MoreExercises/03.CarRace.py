n = input().split(" ")
first_car = 0
second_car = 0
for i in range(0, len(n) // 2):
    first_car += int(n[i])
    if int(n[i]) == 0:
        first_car *= 0.8
for i in range(len(n) - 1, len(n)//2, -1):
    second_car += int(n[i])
    if int(n[i]) == 0:
        second_car *= 0.8
min_time = min(first_car, second_car)
if min_time == first_car:
    side = "left"
else:
    side = "right"
print(f"The winner is {side} with total time: {min_time:.1f}")