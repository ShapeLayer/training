def compute(n: int, gets: list[int]) -> int:
    total = 0
    for get in gets:
        total += min(n, get)
    return total

if __name__ == '__main__':
    n = int(input())
    gets: list[int] = list(map(int, input().split()))
    print(compute(n, gets))
