def compute(n: int, arr: list[int]) -> int:
    cnt = 0
    for i in range(n):
        if i + 1 != arr[i]:
            cnt += 1
    return cnt

if __name__ == '__main__':
    n = int(input())
    arr: list[int] = list(map(int, input().split()))
    print(compute(n, arr))
