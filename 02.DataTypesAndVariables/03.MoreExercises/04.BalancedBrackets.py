def is_balanced(count):
    for i in range(0, len(count), 2):
        if len(count) % 2 == 0:
            if count[i] == "(" and count[i + 1] == ")":
                return True
            else:
                return False

            
n_lines = int(input())
count = []
for i in range(n_lines):
    s = input()

    if s == "(":
        count.append(s)
    if s == ")":
        count.append(s)

if is_balanced(count):
    print("BALANCED")
else:
    print("UNBALANCED")
