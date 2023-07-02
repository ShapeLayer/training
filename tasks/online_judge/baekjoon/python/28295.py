def compute(opers: list[int]) -> int:
    '''
            리버스  가로 여부
        0   0       0   북
        1   0       1   동
        2   1       0   남
        3   1       1   서
    '''
    curr = 0
    for oper in opers:
        if oper == 1:
            curr = (curr + 1) % 4
        elif oper == 2:
            curr ^= 2
        else:
            curr = (curr - 1) % 4
    return curr

if __name__ == '__main__':
    opers: list[int] = [int(input()) for _i in range(10)]
    print('NESW'[compute(opers)])
