def compute(n: int, arr: list[int]) -> int:
    count = 0
    for i in range(n):
        if arr[i - 1] >= arr[i]:
            count += 1
    return count

if __name__ == '__main__':
    n = int(input())
    arr: list[int] = list(map(int, input().split()))
    print(compute(n, arr))
