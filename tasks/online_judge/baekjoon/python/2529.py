MAX = int(1e10)
MIN = -MAX

def compute(n: int, comparators: list[str]) -> tuple[str]:
    used: list[bool] = [False for _i in range(10)]

    def evalute(prev: int, now: int, step: int):
        return (prev < now) == (comparators[step] == '<')

    def generate_arr(buf: list[int], step: int, mx: int, mn: int):
        if len(buf) == n:
            result = 0
            for each in buf:
                result *= 10
                result += each
            return result, result
        for i in range(10):
            if not used[i]:
                if not evalute(buf[-1], i, step): continue
                used[i] = True
                resmx, resmn = generate_arr(buf + [i], step + 1, mx, mn)
                used[i] = False
                if mx < resmx:
                    mx = resmx
                if mn > resmn:
                    mn = resmn
        return mx, mn

    mx, mn = MIN, MAX
    for i in range(10):
        used[i] = True
        resmx, resmn = generate_arr([i], 0, mx, mn)
        if mx < resmx:
            mx = resmx
        if mn > resmn:
            mn = resmn
        used[i] = False
    return mx, mn

if __name__ == '__main__':
    n = int(input())
    n += 1
    comparators: list[str] = input().split()
    resmx, resmn = compute(n, comparators)
    print(str(resmx).zfill(n))
    print(str(resmn).zfill(n))
