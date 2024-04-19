s = input().split(", ")
for i in range(len(s)):
    if i == len(s) - 1 and s[i] == "wolf":
        print("Please go away and stop eating my sheep")
    elif s[i] == "wolf" and i != len(s):
        print(f"Oi! Sheep number {len(s) - i - 1}! You are about to be eaten by a wolf!")
