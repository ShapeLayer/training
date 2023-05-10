def compute(arr: list[int]) -> int:
    result = min(arr)
    while True:
        cnt = 0
        for n in arr:
            if result % n == 0:
                cnt += 1
        if cnt > 2:
            return result
        result += 1

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(compute(arr))
