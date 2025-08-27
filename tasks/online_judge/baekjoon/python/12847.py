N, M = map(int, input().split())
T = [*map(int, input().split())]

total_earn = sum(T[0:M])
maximum_earn = total_earn

for i in range(M, N):
    total_earn += T[i]
    total_earn -= T[i - M]
    maximum_earn = max(maximum_earn, total_earn)

print(maximum_earn)
