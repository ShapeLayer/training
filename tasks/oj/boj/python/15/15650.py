n, m = map(int, input().split())
results = []
def proc(collected, remains):
    global results
    if len(collected) == m and set(collected) not in results:
        print(' '.join(map(str, collected)))
        results += [set(collected)]
        return
    for i in range(len(remains)):
        now = remains.pop(0)
        proc(collected + [now], remains)
        remains += [now]
proc([], [i for i in range(1, n+1)])