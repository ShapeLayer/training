from sys import stdin
input = stdin.readline

def proc(n: int, arr: list) -> list:
    dt = int(3e10)
    result = []

    if n == 3: return arr
    for _i in range(n - 2):
        # 하나 고정한 채 투포인터이나,
        # 이미 한번 고정해서 탐색했으면 다음부터 사용할 일 없음
        select = arr.pop()
        l, r = 0, len(arr) - 1
        while l < r:
            now = select + arr[l] + arr[r]
            if abs(dt) > abs(now):
                dt = now
                result = sorted([select, arr[l], arr[r]])
            if now < 0: l += 1
            else: r -= 1
            if dt == 0: return result
        if dt == 0: return result
    return result

if __name__ == '__main__':
    n = int(input())
    arr = sorted(list(map(int, input().split())))
    print(*proc(n, arr))
