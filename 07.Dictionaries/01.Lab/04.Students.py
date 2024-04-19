total = {}
for i in range(4):
    student = input().split(":")
    total[student[0]] = student[1], student[2]
program = input()
new = {}
for i1 in total.items():
    if program in i1[1]:
        value = 0
        for i in i1[1]:
            if i.isdigit():
                value = i
        new[i1[0]] = value

for i in new.items():
    print(f"{i[0]} - {i[1]}")
