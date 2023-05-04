from sys import stdin
input = stdin.readline

def proc(n: int, arr: list) -> list:
    dt = int(3e10)
    result = []

    if n == 2: return arr
    l, r = 0, len(arr) - 1
    while l < r:
        now = arr[l] + arr[r]
        if abs(dt) > abs(now):
            dt = now
            result = sorted([arr[l], arr[r]])
        if now < 0: l += 1
        else: r -= 1
        if dt == 0: return result
    if dt == 0: return result
    return result

if __name__ == '__main__':
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    print(*proc(n, arr))
