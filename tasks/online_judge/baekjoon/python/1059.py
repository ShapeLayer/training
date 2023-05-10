def compute(l: int, arr: list[int], n: int):
    arr.append(-1)
    arr.sort()

    result = 0
    for i in range(l - 1):
        if arr[i] == n or arr[i + 1] == n:
            result = 0
            break
        if arr[i] < n < arr[i + 1]:
            result = (n - arr[i]) * (arr[i + 1] - n) - 1
            break
    return result

if __name__ == '__main__':
    l = int(input())
    arr = list(map(int, input().split()))
    n = int(input())
    print(compute(l, arr, n))
