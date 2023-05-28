def compute(n: int, t: int, req: list[int]) -> int:
    elapsed, count = 0, 0
    for r in req:
        if r + elapsed <= t:
            elapsed += r
            count += 1
        else:
            break
    return count

if __name__ == '__main__':
    n, t = map(int, input().split())
    req = list(map(int, input().split()))
    print(compute(n, t, req))
