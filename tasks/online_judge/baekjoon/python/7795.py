from sys import stdin
input = stdin.readline

def compute(a: int, b: int, arr_a: list[int], arr_b: list[int]):
    arr_a.sort(reverse=True)
    arr_b.sort(reverse=True)
    count = 0
    pa, pb = 0, 0
    while pa < a and pb < b:
        if arr_a[pa] > arr_b[pb]:
            count += b - pb
            pa += 1
        else:
            pb += 1
    return count

if __name__ == '__main__':
    for _i in range(int(input())):
        a, b = map(int, input().split())
        arr_a = [*map(int, input().split())]
        arr_b = [*map(int, input().split())]
        print(compute(a, b, arr_a, arr_b))
