N = int(input())
X = [*map(int, input().split())]
T = [*map(int, input().split())]


elapsed = X[-1]
prev_pos = X[-1]

for i in range(N - 1, -1, -1):
    pos = X[i]
    ti = T[i]
    
    elapsed += prev_pos - pos

    if elapsed < ti:
        elapsed = ti

    prev_pos = pos

elapsed += prev_pos

print(elapsed)
