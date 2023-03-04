for _i in range(int(input())):
    p, m = map(int, input().split())
    arr = [False] * (m+1)
    cnt = 0
    for _i in range(p):
        now = int(input())
        if not arr[now]:
            arr[now] = True
        else:
            cnt += 1
    print(cnt)
