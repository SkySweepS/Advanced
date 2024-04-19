def inventory_search(inventory):
    for key, value in inventory.items():
        if int(value) >= 250:
            print(inventory[key])
            print(inventory[value])
            break

inventory = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}

name = ""
junk = {}
while name == "":
    for key, value in inventory.items():
        if value >= 250:
            if key == "shards":
                inventory[key] -= 250
                name = "Shadowmourne"
                break
            elif key == "fragments":
                inventory[key] -= 250
                name = "Valanyr"
                break
            elif key == "motes":
                inventory[key] -= 250
                name = "Dragonwrath"
                break
    if name != "":
        print(f"{name} obtained!")
        for key, value in inventory.items():
            print(f"{key}: {value}")
        for key1, value1 in junk.items():
            print(f"{key1}: {value1}")
        break
    else:
        items = input().lower().split(" ")
        for i in range(1, len(items), 2):
            if items[i] in inventory.keys():
                inventory[items[i]] += int(items[i - 1])
                n = inventory[items[i]]
                if n >= 250:
                    break
            else:
                if items[i] not in junk.keys():
                    junk[items[i]] = int(items[i - 1])
                else:
                    junk[items[i]] += int(items[i - 1])

