from sys import stdin
input = stdin.readline

def compute(n: int, s: int, d: int, d_arr: list[int], v_arr: list[int]) -> int:
    result = 0
    for i in range(n):
        di, vi = d_arr[i], v_arr[i]
        if d * s >= di:
            result += vi
    return result

if __name__ == '__main__':
    k = int(input())
    for t in range(k):
        n, s, d = map(int, input().split())
        d_arr, v_arr = [], []
        for i in range(n):
            di, vi = map(int, input().split())
            d_arr.append(di)
            v_arr.append(vi)
        print(f'Data Set {t + 1}:')
        print(compute(n, s, d, d_arr, v_arr))
        print()
