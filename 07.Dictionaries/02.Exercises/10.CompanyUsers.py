add_employee = {}

while True:
    inp = input()
    if inp == "End":
        break
    info = inp.split("->")

    if info[0] not in add_employee:
        add_employee[info[0]] = info[1]
    else:
        true = False
        if info[1] in add_employee[info[0]]:
            true = True
        if not true:
            add_employee[info[0]] += info[1]

for key, value in add_employee.items():
    v = add_employee[key].strip().split(" ")
    print(key)
    for i in v:
        print(f"-- {i}")
