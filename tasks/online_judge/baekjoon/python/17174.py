n, m = map(int, input().split())
res = n
while n:
    n //= m
    res += n
print(res)
