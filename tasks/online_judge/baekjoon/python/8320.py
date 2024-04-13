n = int(input())
print(sum([(n // i) + int(i ** 2 <= n) for i in range(1, n + 1)]) // 2)
