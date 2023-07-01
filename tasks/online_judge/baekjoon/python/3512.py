from collections import defaultdict
def compute(n: int, c: int, arr: list[tuple]) -> tuple[float]:
    table = defaultdict(lambda: 0)
    total: int = 0
    for each in arr:
        size, _type = each
        table[_type] += size
        total += size
    return total, table['bedroom'], table['balcony'] / 2

if __name__ == '__main__':
    n, c = map(int, input().split())
    arr: list[tuple] = []
    for _i in range(n):
        gets = input().split()
        arr.append((int(gets[0]), gets[1]))
    result = compute(n, c, arr)
    print(result[0])
    print(result[1])
    print(c * (result[0] - result[2]))
