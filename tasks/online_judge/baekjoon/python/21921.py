from sys import stdin
input = stdin.readline

def compute(n: int, x: int, daily: list[int]) -> tuple[int]:
    max_daily, repeats = sum(daily[0:x]), 1
    _range = max_daily
    for l in range(n - x):
        _range += daily[l + x] - daily[l]
        if max_daily < _range:
            max_daily = _range
            repeats = 1
        elif max_daily == _range:
            repeats += 1
    return max_daily, repeats

if __name__ == '__main__':
    n, x = map(int, input().split())
    daily = [*map(int, input().split())]
    m, r = compute(n, x, daily)
    if m:
        print(m)
        print(r)
    else:
        print('SAD')
