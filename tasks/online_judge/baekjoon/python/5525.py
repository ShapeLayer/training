def compute(n: int, m: int, s: str) -> int:
    idx, prev, count = 0, 0, 0
    while idx + 3 <= m:
        if s[idx:idx + 3] == 'IOI':
            prev += 1
            idx += 2
        else:
            count += max(prev - (n - 1), 0)
            prev = 0
            idx += 1
    count += max(prev - (n - 1), 0)
    return count

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    s = input()
    print(compute(n, m, s))
