from collections import deque


def supermarket():
    s = deque([])
    while True:
        name = input()
        if name == "Paid":
            for i in range(len(s)):
                print(s.popleft())

        elif name == "End":
            print(f"{len(s)} people remaining.")
            break
        else:
            s.append(name)


supermarket()
