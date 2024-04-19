n = input()
largest = []
string = ""
for i in range(len(n)):
    largest.append(int(n[i]))
largest.sort()
new = list(reversed(largest))
for i in new:
    string += str(i)
print(string)