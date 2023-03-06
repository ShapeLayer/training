n, m = map(int, input().split())
[input() for _i in range(n+m)]
print(''.join([str(i % 5 + 1) for i in range(n)]))
