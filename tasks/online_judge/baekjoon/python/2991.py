def compute(a: int, b: int, c: int, d: int, p: int, m: int, n: int) -> tuple[int]:
    first = a + b
    second = c + d
    buf = []
    for each in (p, m, n):
        cnt = 0
        if 0 < each % first <= a:
            cnt += 1
        if 0 < each % second <= c:
            cnt += 1
        buf.append(cnt)
    return buf

if __name__ == '__main__':
    a, b, c, d = map(int, input().split())
    p, m, n = map(int, input().split())
    for each in compute(a, b, c, d, p, m, n):
        print(each)
