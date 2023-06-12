def compute(n: int, logs: list[tuple[int]]) -> int:
    enters = {}
    skipped = 0
    for log in logs:
        a, b = log
        if b == 1:
            if a in enters:
                if enters[a]:
                    skipped += 1
            enters[a] = True
        else:
            if a not in enters:
                skipped += 1
            else:
                if not enters[a]:
                    skipped += 1
            enters[a] = False
    for each in enters:
        if enters[each]:
            skipped += 1
    return skipped

if __name__ == '__main__':
    n = int(input())
    logs: list[tuple[int]] = [tuple(map(int, input().split())) for _i in range(n)]
    print(compute(n, logs))
