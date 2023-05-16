d1, d2 = list(map(int, input().split()))
d = d2 - d1

n = int(d**0.5)

if n == 1:
    print(d)
elif d == n**2:
    print(2*n-1)
elif d >= n*(n+1)+1:
    print(2*n+1)
elif d >= n**2+1:
    print(2*n)
