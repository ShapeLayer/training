pnt = [100, 100]
for _ in range(int(input())):
    n1, n2 = list(map(int, input().split()))
    if n1 > n2:
        pnt[1] -= n1
    elif n1 < n2:
        pnt[0] -= n2
print(pnt[0])
print(pnt[1])