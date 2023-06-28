def compute(n: int, gets: list[int]) -> list[int]:
    arr = [i + 1 for i in range(n)]
    for i in range(n):
        now = gets[i]
        for j in range(i, i - now, -1):
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr

if __name__ == '__main__':
    n = int(input())
    gets: list[int] = list(map(int, input().split()))
    print(*compute(n, gets))
