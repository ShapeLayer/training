DATES = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def compute(m: int, d: int) -> str:
    elapsed = sum(DATES[0:m]) + d
    return DAYS[(elapsed + 2) % 7 ]

if __name__ == '__main__':
    d, m = map(int, input().split())
    print(compute(m, d))
