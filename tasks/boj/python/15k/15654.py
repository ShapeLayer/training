from sys import stdout
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

visited = [False for i in range(n)]
outs = []

def processing(depth, n, m):
    if depth == m:
        print(' '.join(map(str, outs)))
        return 0
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            outs.append(arr[i])
            processing(depth + 1, n, m)
            outs.pop()
            visited[i] = False

processing(0, n, m)