cnt = 0
for _ in range(10):
    n = int(input())
    if n % 3 == 0:
        cnt += n
print(cnt)