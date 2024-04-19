s = input().lower()     #input mixed word
count = 0
for i in range(len(s)):
    if s[i:i+4] == "sand":
        count += 1
    if s[i:i+5] == "water":
        count += 1
    if s[i:i+4] == "fish":
        count += 1
    if s[i:i+3] == "sun":
        count += 1
print(count)