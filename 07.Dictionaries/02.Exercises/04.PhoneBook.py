phone_book = {}
check = 0
while True:
    line = input()
    if line.isdigit():
        check = int(line)
        break
    line = line.split("-")
    phone_book[line[0]] = line[1]
for i in range(check):
    name = input()
    if name in phone_book.keys():
        print(f"{name} -> {phone_book[name]}")
    else:
        print(f"Contact {name} does not exist.")
