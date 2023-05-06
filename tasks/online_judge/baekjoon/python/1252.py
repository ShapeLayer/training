def compute(a: str, b: str) -> int:
    max_len = max(len(a), len(b))
    a, b = a.zfill(max_len), b.zfill(max_len)
    c = ''
    is_carry = False
    for i in range(-1, -max_len - 1, -1):
        now = int(is_carry)
        now += int(a[i]) + int(b[i])
        is_carry = now // 2 == 1
        now %= 2
        c = str(now) + c
    if is_carry:
        c = '1' + c
    return c

if __name__ == '__main__':
    print(compute(*input().split()))
