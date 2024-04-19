country = input().split(", ")
capital = input().split(", ")
new_dict = {}
for i in range(len(country)):
    new_dict[country[i]] = capital[i]

for key, value in new_dict.items():
    print(f"{key} -> {value}")
