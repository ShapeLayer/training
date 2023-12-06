def compute(n: int) -> str:
    if n >= 97: return 'A+'
    elif n >= 90: return 'A'
    elif n >= 87: return 'B+'
    elif n >= 80: return 'B'
    elif n >= 77: return 'C+'
    elif n >= 70: return 'C'
    elif n >= 67: return 'D+'
    elif n >= 60: return 'D'
    else: return 'F'

if __name__ == '__main__':
    for _i in range(int(input())):
        a, b = input().split()
        print(a, compute(int(b)))
