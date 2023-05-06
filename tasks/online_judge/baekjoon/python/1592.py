def compute(n: int, m: int, l: int) -> int:
    rec = [0 for _i in range(n)]
    idx, cnt = 0, 0
    while rec[idx] != m:
        if rec[idx] % 2 == 0:
            idx = (idx - l) % n
            rec[idx] += 1
            cnt += 1
        else:
            idx = (idx + l) % n
            rec[idx] += 1
            cnt += 1
    return cnt - 1

if __name__ == '__main__':
    n, m, l = map(int, input().split())
    print(compute(n, m, l))
