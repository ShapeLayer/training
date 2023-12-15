def compute(n: int, arr: list[int], _range: list[int]):
    max_range = arr[0]
    for i in range(n - 1):
        now = arr[i] + _range[i]
        max_range = max(now, max_range)
        if max_range < arr[i + 1]:
            return False
    return True

if __name__ == '__main__':
    n = int(input())
    arr: list[int] = [*map(int, input().split())]
    _range: list[int] = []
    if n > 1: _range = [*map(int, input().split())]
    if compute(n, arr, _range):
        print('권병장님, 중대장님이 찾으십니다')
    else:
        print('엄마 나 전역 늦어질 것 같아')
