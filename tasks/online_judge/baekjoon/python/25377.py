MAX: int = int(1e10)

def compute(n: int, td: list[tuple[int]]) -> int:
    result = MAX
    for t in td:
        a, b = t
        if a <= b:
            result = min(result, b)
    return result

if __name__ == '__main__':
    n = int(input())
    td: list[tuple[int]] = [tuple(map(int, input().split())) for _i in range(n)]
    result = compute(n, td)
    print(result if result != MAX else -1)
