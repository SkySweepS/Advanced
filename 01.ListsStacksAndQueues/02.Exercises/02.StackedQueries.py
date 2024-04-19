n = int(input())
stack = []

for _ in range(n):
    querie = input().split(" ")
    command = int(querie[0])
    if command == 1:
        stack.append(int(querie[1]))

    elif command == 2:
        if stack:
            stack.pop()
    elif command == 3:
        if stack:
            print(max(stack))
    elif command == 4:
        if stack:
            print(min(stack))

print(", ".join([str(x) for x in stack[::-1]]))
