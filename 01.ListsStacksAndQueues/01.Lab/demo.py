from collections import deque

n = int(input())
houses = [i for i in range(n)]
safeHouse = [int(i) for i in input().split()]


houses = deque(houses)
count = 0
max_b = 0
ch= 0
lst =[]
while houses:
	check = houses.popleft()
	if check in safeHouse:
		su = safeHouse.pop()
		ch += 1
		
		count = 0
	else:
		count += 1
	if count > max_b:
		max_b = count
		lst.append(count)
		
max_b = max(lst)		
if ch > 1:
	new = round(max_b/2)
else:
	new = max_b


		
print(new)
	
	
	

print(lst)