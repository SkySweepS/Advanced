key = int(input())
n_lines = int(input())
result = ""
for i in range(n_lines):
    s = input()
    result += chr(ord(s) + key)
print(result)
