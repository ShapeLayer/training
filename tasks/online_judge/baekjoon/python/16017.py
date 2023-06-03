def compute(gets: list[int]) -> bool:
    return gets[0] in (8, 9) and gets[3] in (8, 9) and gets[1] == gets[2]

if __name__ == '__main__':
    gets = [int(input()) for _ in range(4)]
    print('ignore' if compute(gets) else 'answer')
