from sys import stdin
input = stdin.readline

def compute(x: float, y: float) -> str:
    if x == 0 or y == 0:
        return 'AXIS'
    if x > 0 and y > 0:
        return 'Q1'
    if x < 0 and y > 0:
        return 'Q2'
    if x < 0 and y < 0:
        return 'Q3'
    if x > 0 and y < 0:
        return 'Q4'

if __name__ == '__main__':
    while True:
        x, y = map(float, input().split())
        print(compute(x, y))
        if x == y == 0:
            break
