def compute(ca: int, ba: int, pa: int, cr: int, br: int, pr: int) -> int:
    return max(0, cr - ca) + max(0, br - ba) + max(0, pr - pa)

if __name__ == '__main__':
    ca, ba, pa = map(int, input().split())
    cr, br, pr = map(int, input().split())
    print(compute(ca, ba, pa, cr, br, pr))
