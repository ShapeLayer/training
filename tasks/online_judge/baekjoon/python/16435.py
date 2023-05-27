def compute(n: int, l: int, fruits: list[int]) -> int:
    for fruit in fruits:
        if l >= fruit:
            l += 1
    return l

if __name__ == '__main__':
    n, l = map(int, input().split())
    fruits: list[int] = sorted(list(map(int, input().split())))
    print(compute(n, l, fruits))
