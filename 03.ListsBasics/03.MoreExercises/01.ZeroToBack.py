s = input().split(", ")
for i in s:
    if int(i) == 0:
        s.remove(i)
        s.append(i)
s_1 = []
for i in s:
    s_1.append(int(i))
print(s_1)
