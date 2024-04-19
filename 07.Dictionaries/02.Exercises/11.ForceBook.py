

user_side = {}
while True:
    force = input()
    if force == "Lumpawaroo":
        break
    temp_force = force.split(" ")

    for i in temp_force:
        if i == "|":
            force = force.split(" | ")

            if force[0] not in user_side:
                user_side[force[0]] = [force[1]]
                break
            else:
                user_side[force[0]] += [force[1]]
                break
        elif i == "->":
            force = force.split(" -> ")
            if force[0] in user_side.values():
                print(f"{force}")
                print(user_side.values())





for key, value in user_side.items():
    if len(user_side[key]) > 0:
        print(f"Side: {key}, Members: {len(user_side[key])}")
        for i in value:
            print(f"! {i}")
print(user_side)