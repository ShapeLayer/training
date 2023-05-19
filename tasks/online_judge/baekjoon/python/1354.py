def compute(n: int, p: int, q: int, x: int, y: int) -> int:
    arr = {0: 1}
    def get(idx: int) -> int:
        if idx < 0:
            return 1
        if idx in arr:
            return arr[idx]
        else:
            arr[idx] = get(idx // p - x) + get(idx // q - y)
            return arr[idx]
    return get(n)

if __name__ == '__main__':
    n, p, q, x, y = map(int, input().split())
    print(compute(n, p, q, x, y))
