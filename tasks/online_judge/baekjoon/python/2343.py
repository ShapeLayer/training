def compute(n: int, m: int, runs: list[int]):
    def check(limits: int):
        counts, sums = 0, 0
        for run in runs:
            if run + sums > limits:
                counts += 1
                sums = 0
            sums += run
        if sums > 0:
            counts += 1
        return counts > m
    
    lo, hi = max(runs), sum(runs)
    while lo <= hi:
        mid = (lo + hi) // 2
        if check(mid):
            lo = mid + 1
        else:
            hi = mid - 1
    return lo

if __name__ == '__main__':
    n, m = map(int, input().split())
    runs: list[int] = list(map(int, input().split()))
    print(compute(n, m, runs))
