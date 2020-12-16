n = int(input("Nhập n: "))
list = []
for i in range(n):
	list.append(int(input("Nhập list: ")))
answer = 0
for v in list:
	answer += v
print(answer)