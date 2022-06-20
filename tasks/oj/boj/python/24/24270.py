n, k = map(int, input().split())
gets = list(map(int, input().split()))

def fac(n: int, r: int) -> int:
    res = 1
    for i in range(n, r-1, -1):
        res *= i
        res %= 1000000007
    return res

for get in gets: k -= get - 1
print(fac(k, n))
