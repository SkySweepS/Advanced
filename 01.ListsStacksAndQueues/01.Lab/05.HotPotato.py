from collections import deque


def potato(names, tosses):

    count = 0
    names = deque(names)

    while names:
        count += 1
        person = names.popleft()
        if count == tosses:
            if len(names) > 0:
                print(f"Removed {person}")
            else:
                print(f"Last is {person}")
            count = 0
        else:
            names.append(person)


potato(input().split(" "), int(input()))
