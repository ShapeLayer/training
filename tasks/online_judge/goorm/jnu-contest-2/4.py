n, m = map(int, input().split())
maps = [[-1 for _i in range(n)] for _j in range(m)]
for i in range(n):
	maps[i] = list(map(int, input().split()))
counts = set()
ables = [
	((-1, -1), (-1, 0), (0, -1)),
	((-1, 1), (-1, 0), (0, 1)),
	((1, -1), (1, 0), (0, -1)),
	((1, 1), (1, 0), (0, 1)),
	(-1, 0),
	(0, -1),
	(1, 0),
	(0, 1)
]

for i in range(n):
	for j in range(m):
		l, t, r, b = j-1, i-1, j+1, i+1
		lf, tf, rf, bf = False, False, False, False
		if l < 0:
			l = 0
			lf = True
		if t < 0:
			t = 0
			tf = True
		if r >= n:
			r = n-1
			rf = True
		if b >= m:
			b = m-1
			bf = True
		for k in range(8):
			if lf:
				if k in (0, 2, 5): continue
			if tf:
				if k in (0, 1, 4): continue
			if rf:
				if k in (1, 3, 7): continue
			if bf:
				if k in (2, 3, 6): continue
			if maps[i][j] == 1:
				able = ables[k]
				if k < 4:
					if maps[i+able[0][0]][j+able[0][1]] == 1:
						if not (maps[i+able[1][0]][j+able[1][1]] == 2 and maps[i+able[2][0]][j+able[2][1]] == 2):
							counts.add(i*n+j)
				else:
					if maps[i+able[0]][j+able[1]] == 1:
						counts.add(i*n+j)

print(len(counts))