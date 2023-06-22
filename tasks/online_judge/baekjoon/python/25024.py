from sys import stdin
input = stdin.readline

def date_isable(x: int, y: int) -> bool:
    if x in (1, 3, 5, 7, 8, 10, 12):
        return 1 <= y <= 31
    elif x in (4, 6, 9, 11):
        return 1 <= y <= 30
    elif x == 2:
        return 1 <= y <= 29
    return False

def time_isable(x: int, y: int) -> bool:
    return 0 <= x < 24 and 0 <= y < 60

def compute(x: int, y: int) -> tuple[bool]:
    return date_isable(x, y), time_isable(x, y)

if __name__ == '__main__':
    for _t in range(int(input())):
        d, t = compute(*map(int, input().split()))
        print('Yes' if t else 'No', 'Yes' if d else 'No')
