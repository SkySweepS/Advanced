box_of_clothes = input().split(" ")
rack_capacity = int(input())
capacity = rack_capacity
count = 1
while box_of_clothes:
    clothes = box_of_clothes.pop()

    if capacity - int(clothes) >= 0:
        capacity -= int(clothes)
    else:
        box_of_clothes.append(str(clothes))
        capacity = rack_capacity
        count += 1

print(count)
