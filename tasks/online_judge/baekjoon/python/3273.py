def compute(n: int, arr: list[int], x: int) -> int:
    count = 0
    arr.sort()
    l, r = 0, n - 1
    while l < r:
        now = arr[l] + arr[r]
        if now > x:
            r -= 1
        elif now < x:
            l += 1
        else:
            count += 1
            l += 1
    return count

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    x = int(input())
    print(compute(n, arr, x))
