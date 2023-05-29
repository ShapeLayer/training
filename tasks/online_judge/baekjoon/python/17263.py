def compute(n: int, arr: list[int]) -> int:
    return sorted(arr)[-1]

if __name__ == '__main__':
    n = int(input())
    arr: list[int] = list(map(int, input().split()))
    print(compute(n, arr))
