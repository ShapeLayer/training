from sys import stdin
input = stdin.readline

def compute(arr: list[tuple[int]]) -> float:
    sums = 0
    for i in range(n):
        sums += arr[i % n][0] * arr[(i + 1) % n][1]
        sums -= arr[(i + 1) % n][0] * arr[i % n][1]
    return abs(sums / 2)

if __name__ == '__main__':
    n = int(input())
    dots = [tuple(map(int, input().split())) for _i in range(n)]
    print(compute(dots))
