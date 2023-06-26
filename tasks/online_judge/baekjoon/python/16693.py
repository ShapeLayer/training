from math import pi

def compute(a1: int, p1: int, r1: int, p2: int) -> bool:
    return p1 / a1 < p2 / (r1 ** 2 * pi)

if __name__ == '__main__':
    (a1, p1), (r1, p2) = map(int, input().split()), map(int, input().split())
    if compute(a1, p1, r1, p2):
        print('Slice of pizza')
    else:
        print('Whole pizza')
