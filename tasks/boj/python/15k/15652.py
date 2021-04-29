n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]

outs = []

def processing(depth, before):
    if depth == m:
        print(' '.join(map(str, outs)))
        return 0
    for i in range(n):
        if before <= arr[i]:
            outs.append(arr[i])
            processing(depth + 1, arr[i])
            outs.pop()

processing(0, 0)