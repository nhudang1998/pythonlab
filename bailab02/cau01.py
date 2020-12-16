n = int(input("Nhập n: "))
list = []
for i in range(n):
	list.append(int(input("Nhập list: ")))
min_value = list[0]
for i in list:
	if i < min_value:
		min_value = i
print(min_value)