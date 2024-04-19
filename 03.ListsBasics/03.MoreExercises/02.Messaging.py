

n_list = input().split(" ")
string = input()
int_list = []
for i in n_list:
    count = 0
    for i1 in i:
        count += int(i1)
    int_list.append(count)
decode = ""
for i in int_list:
    if i < len(string):
        decode += string[i]
        string = string.replace(string[i], "", 1)

    else:
        i = i - len(string)
        decode += string[i]
        string = string.replace(string[i], "")

print(decode)