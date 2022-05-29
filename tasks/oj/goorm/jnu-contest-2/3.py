n = int(input())
gets = list(map(int, input().split()))
counts = set()

for case in range(2, int(max(gets)**.5)):
	flag = True
	for mins in range(int(min(gets))):
		flag = True
		for col in gets:
			if col % case != mins or col < mins:
				flag = False
				break
		if flag:
			break
	if flag: counts.add(case)
print(len(counts))