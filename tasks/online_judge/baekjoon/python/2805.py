def compute(n: int, m: int, trees: list[int]):
    def check(mid: int) -> bool:
        return sum([tree - mid if tree > mid else 0 for tree in trees]) >= m
    low, high = 0, int(1e10)
    while low + 1 < high:
        mid: int = (low + high) // 2
        if check(mid):
            low = mid
        else:
            high = mid
    return low

if __name__ == '__main__':
    n, m = map(int, input().split())
    trees: list[int] = list(map(int, input().split()))
    print(compute(n, m, trees))
