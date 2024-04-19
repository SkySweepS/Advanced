number_list = input().split(" ")
k = int(input())
result = []

while True:
    if len(number_list) == 0:
        break
    n = k
    for i in range(len(number_list)):
        if n > len(number_list):
            n -= len(number_list)

        if i + 1 == n:
            result.append(int(number_list[i]))
            n += k
        for i1 in result:
            if str(i1) in number_list:
                number_list.remove(str(i1))


    """for i1 in result:
        if str(i1) in number_list:
            number_list.remove(str(i1))"""


print(number_list)
print(result)



