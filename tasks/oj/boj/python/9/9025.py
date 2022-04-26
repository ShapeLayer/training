from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    spots = []
    n = int(input())
    conn = [[] for _ in range(n+2)]
    for i in range(n+2):
        spots += [list(map(int, input().split()))]
    for i in range(n+2):
        for j in range(n+2):
            if i == j:
                continue
            distance = abs(spots[i][0] - spots[j][0]) + abs(spots[i][1] - spots[j][1])
            if distance <= 50 * 20:
                conn[i] += [j]
                conn[j] += [i]
    visits = [False for _ in range(n+2)]
    visits[0] = True
    queue = [0]
    while queue:
        now = queue.pop(0)
        for next in conn[now]:
            if not visits[next]:
                queue.append(next)
                visits[next] = True
    if visits[len(visits)-1]:
        print('happy')
    else:
        print('sad')
