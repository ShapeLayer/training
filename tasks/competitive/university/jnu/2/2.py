maps = [['' for _i in range(3)] for _j in range(3)]
for i in range(3):
	gets = input()
	for j in range(3):
		maps[i][j] = gets[j]
corrects = [
	((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
	((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
	((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0))
]

flag = False
for corr in corrects:
	if maps[corr[0][0]][corr[0][1]] == maps[corr[1][0]][corr[1][1]] == maps[corr[2][0]][corr[2][1]] and maps[corr[0][0]][corr[0][1]] != '.':
		flag = True

print('YES' if flag else 'NO')