def compute(a: str, b: str) -> int:
    _a: list[int] = [int(i) for i in a]
    _b: list[int] = [int(i) for i in b]

    result = 0
    for i in _a:
        for j in _b:
            result += i * j
    return result

if __name__ == '__main__':
    print(compute(*input().split()))
