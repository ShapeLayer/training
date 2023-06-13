def compute(a: float, b: float, c: float) -> float:
    return a * b * c

if __name__ == '__main__':
    for _t in range(int(input())):
        print('$%.2f' % compute(*map(float, input().split())))
