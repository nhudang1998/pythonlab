list = []
n = int(input("nhập n: "))
for i in range(n):
	list.append(int(input("nhập list: ")))
answer = []
for v in list:
	if v % 2 != 0:
		answer.append(v)
print(answer)