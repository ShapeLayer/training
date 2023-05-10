from sys import stdin
input = stdin.readline

def compute(n: int, arr: list[int]) -> list[int]:
    arr_sorted = sorted(arr)
    idx = {}
    for i in range(n):
        if arr_sorted[i] not in idx:
            idx[arr_sorted[i]] = [i]
        else:
            idx[arr_sorted[i]].append(i)
    result = [idx[i].pop(0) for i in arr]
    return result

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = compute(n, arr)
    print(*result)
