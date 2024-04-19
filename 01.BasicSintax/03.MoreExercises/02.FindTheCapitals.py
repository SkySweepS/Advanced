n = input()
n_list = []

for i1 in range(ord('A'), ord('Z')):
    for i in range(len(n)):
        if n[i] == chr(i1):
            n_list.append(i)
print(sorted(n_list))
