from collections import deque


def water_dispenser(water):
    que = deque([])
    while True:
        names = input()
        if names == "Start":
            break
        que.append(names)
    while True:
        tap_out = input().split(" ")
        if tap_out[0] == "End":
            print(f"{water} liters left")
            break
        elif tap_out[0] == "refill":
            water += int(tap_out[1])
        else:
            water -= int(tap_out[0])
            if water >= 0:
                print(f"{que.popleft()} got water")
            else:
                print(f"{que.popleft()} must wait")
                water += int(tap_out[0])


water_dispenser(int(input()))
