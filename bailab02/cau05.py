list = []
n = int(input("Nhập n: "))
for i in range(n):
	list.append(int(input("nhập list: ")))
answer = []
for v in list:
	if v % 5 ==0:
		answer.append(v)
if len(answer) == 0:
	answer = [0]
print(answer)