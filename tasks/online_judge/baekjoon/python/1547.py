from sys import stdin
input = stdin.readline

def compute(arr: list[int], a: int, b: int):
    arr[a], arr[b] = arr[b], arr[a]

if __name__ == '__main__':
    n = int(input())
    arr = [None, 1, 0, 0]
    for _i in range(n):
        a, b = map(int, input().split())
        compute(arr, a, b)
    for i in range(1, 4):
        if arr[i] == 1:
            print(i)
