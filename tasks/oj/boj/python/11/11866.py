n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]
res = []

t = k
while arr:
    t = (t-1) % len(arr)
    res += [arr.pop(t)]
    t += k

print('<' + ', '.join(list(map(str, res))) + '>')