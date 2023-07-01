def compute(lw: int, lh: int, sw: int, sh: int) -> int:
    return lw >= sw + 2 and lh >= sh + 2

if __name__ == '__main__':
    lw, lh, sw, sh = map(int, input().split())
    print(int(compute(lw, lh, sw, sh)))
