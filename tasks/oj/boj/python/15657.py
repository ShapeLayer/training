n, m = map(int, input().split())
gets = sorted(list(map(int, input().split())))

def proc(collected):
    if len(collected) == m:
        print(' '.join(map(str, collected)))
        return
    for get in gets:
        if collected:
            if collected[-1] > get:
                continue
        collected += [get]
        proc(collected)
        collected.pop()

proc([])