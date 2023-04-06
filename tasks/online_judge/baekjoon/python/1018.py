n, m = map(int, input().split()) # m 가로 n 세로
plane = [['-']*m]*n
for i in range(n):
    plane[i] = list(input())

counts = []
for i in range(n-7):
    for j in range(m-7):
        for mask in ['WB', 'BW']:
            count = 0
            for a in range(8):
                for b in range(8):
                    ni, nj = i+a, j+b
                    if plane[ni][nj] != mask[(a+b)%2]: count += 1
            counts += [count]
print(min(counts))