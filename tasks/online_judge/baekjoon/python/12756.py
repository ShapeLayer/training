def compute(atk1: int, hp1: int, atk2: int, hp2: int) -> int:
    a, b = hp1 // atk2 + (1 if hp1 % atk2 != 0 else 0), hp2 // atk1 + (1 if hp2 % atk1 != 0 else 0)
    return -a + b

if __name__ == '__main__':
    (atk1, hp1), (atk2, hp2) = map(int, input().split()), map(int, input().split())
    result = compute(atk1, hp1, atk2, hp2)
    if result < 0:
        print('PLAYER A')
    elif result > 0:
        print('PLAYER B')
    else:
        print('DRAW')
