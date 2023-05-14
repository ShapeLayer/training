from sys import stdin
input = stdin.readline

MONTH_TABLE = [0, 31, -1, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def compute(d: int, m: int, y: int):
    def is_leap_year(year: int):
        return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
    result = 0
    for i in range(1, m):
        if i == 2:
            if is_leap_year(y):
                result += 29
            else:
                result += 28
        else:
            result += MONTH_TABLE[i]
    result += d
    return result

if __name__ == '__main__':
    while True:
        d, m, y = map(int, input().split())
        if d == m == y == 0:
            break
        print(compute(d, m, y))
