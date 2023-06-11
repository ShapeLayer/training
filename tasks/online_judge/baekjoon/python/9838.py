def compute(n: int, arr: list[int]) -> list[int]:
    buf = [-1 for _i in range(n)]
    for i in range(n):
        buf[arr[i] - 1] = i + 1
    return buf

if __name__ == '__main__':
    n = int(input())
    arr = [int(input()) for _i in range(n)]
    for each in compute(n, arr):
        print(each)
