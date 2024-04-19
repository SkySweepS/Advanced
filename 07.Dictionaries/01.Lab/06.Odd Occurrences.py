words = input().split(" ")
dic = {}
for i in words:
    word_lower = i.lower()
    if word_lower not in dic:
        dic[word_lower] = 0
    dic[word_lower] += 1
for i1 in dic.items():
    if i1[1] % 2 != 0:
        print(i1[0], end=" ")