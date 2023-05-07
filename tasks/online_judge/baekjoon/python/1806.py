from sys import stdin
input = stdin.readline

def compute(n: int, s: int, arr: list[int]):
    l, r = 0, 0
    result = int(1e10)
    now = 0
    while True:
        if now >= s:
            dist = r - l
            if dist < result:
                result = dist
            now -= arr[l]
            l += 1
        elif r == n:
            # now < s and r positioned at end
            break
        else:
            now += arr[r]
            r += 1
    return result

if __name__ == '__main__':
    n, s = map(int, input().split())
    arr: list[int] = list(map(int, input().split()))
    res = compute(n, s, arr)
    if res == int(1e10): print(0)
    else: print(res)
