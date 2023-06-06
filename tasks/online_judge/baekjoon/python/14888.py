MAX = int(1e10)
MIN = -MAX

def compute(n: int, arr: list[int], remains: list[int]) -> tuple[int]:
    def calculate(prev: int, now: int, operator: int) -> int:
        if operator == 0:
            return prev + now
        if operator == 1:
            return prev - now
        if operator == 2:
            return prev * now
        if operator == 3:
            if prev < 0:
                return -((-prev) // now)
            return prev // now
    def step(calced: int, idx: int, remains: list[int], mx: int, mn: int):
        if idx == n:
            if mx < calced:
                mx = calced
            if mn > calced:
                mn = calced
            return mx, mn
        for i in range(4):
            if remains[i]:
                remains[i] -= 1
                resmx, resmn = step(calculate(calced, arr[idx], i), idx + 1, remains, mx, mn)
                remains[i] += 1
                if mx < resmx:
                    mx = resmx
                if mn > resmn:
                    mn = resmn
        return mx, mn
    mx, mn = step(arr[0], 1, remains, MIN, MAX)
    return mx, mn

if __name__ == '__main__':
    n = int(input())
    arr: list[int] = list(map(int, input().split()))
    remains: list[int] = list(map(int, input().split()))
    mx, mn = compute(n, arr, remains)
    print(mx)
    print(mn)
