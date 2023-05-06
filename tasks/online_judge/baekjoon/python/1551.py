def compute(k, arr: list[int]) -> list[int]:
    for _k in range(k):
        new = []
        for i in range(len(arr) - 1):
            new.append(arr[i + 1] - arr[i])
        arr = new
    return arr

if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split(',')))
    print(','.join(map(str, compute(k, arr))))
