def compute(ates: list[int]) -> int:
    result = 0
    m = max(ates)
    for ate in ates:
        result += (m - ate)
    return result

if __name__ == '__main__':
    ates: list[int] = list(map(int, input().split()))
    print(compute(ates))
