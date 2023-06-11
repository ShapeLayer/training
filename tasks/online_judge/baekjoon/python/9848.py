def compute(n: int, k: int, gets: list[int]) -> int:
    result = 0
    for i in range(n - 1):
        if gets[i] - gets[i + 1] >= k:
            result += 1
    return result

if __name__ == '__main__':
    n, k = map(int, input().split())
    gets = [int(input()) for _i in range(n)]
    print(compute(n, k, gets))
