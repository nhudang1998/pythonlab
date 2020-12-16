list = []
n=int(input("Nhập n: "))
for i in range(n):
	list.append(int(input("nhập list: ")))
for i in range(len(list)):
	for j in range(i):
		if list[i] < list[j]:
			tmp = list[i]
			list[i] = list[j]
			list[j] = tmp
print(list)