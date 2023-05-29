def compute(br: int, bc: int, dr: int, dc: int, jr: int, jc: int) -> int:
    b = max(abs(jr - br), abs(jc - bc))
    d = abs(jr - dr) + abs(jc - dc)
    return b - d

if __name__ == '__main__':
    br, bc = map(int, input().split())
    dr, dc = map(int, input().split())
    jr, jc = map(int, input().split())
    result = compute(br, bc, dr, dc, jr, jc)
    if result < 0:
        print('bessie')
    elif result > 0:
        print('daisy')
    else:
        print('tie')
