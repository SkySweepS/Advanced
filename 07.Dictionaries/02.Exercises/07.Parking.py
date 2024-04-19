n = int(input())
reg_log = {}
for i in range(n):
    register = input().split(" ")
    if register[0] == "register":
        if register[1] not in reg_log:
            reg_log[register[1]] = register[2]
            print(f"{register[1]} registered {register[2]} successfully")
        elif register[2] in reg_log.values():
            print(f"ERROR: already registered with plate number {register[2]}")
    elif register[0] == "unregister":
        if register[1] in reg_log:
            reg_log.pop(register[1])
            print(f"{register[1]} unregistered successfully")
        else:
            print(f"ERROR: user {register[1]} not found")

for key, value in reg_log.items():
    print(f"{key} => {value}")
