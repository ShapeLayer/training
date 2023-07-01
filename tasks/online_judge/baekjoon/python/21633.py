def compute(n: int) -> float:
    if (n * .01 + 25) < 100:
        return 100
    if (n * .01 + 25) > 2000:
        return 2000
    return n * .01 + 25

if __name__ == '__main__':
    print('%.2f' % compute(int(input())))
