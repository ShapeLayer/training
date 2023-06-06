from sys import stdin
input = stdin.readline

def compute(a: int, b: int) -> list[str]:
    result_buf: list[str] = []
    if a == 0:
        result_buf.append('0')
    if a // b != 0:
        result_buf.append(str(a // b))
    if a % b != 0:
        result_buf.append(f'{a % b}/{b}')
    return result_buf

if __name__ == '__main__':
    for t in range(int(input())):
        a, b = map(int, input().split())
        print(f'Case {t + 1}:', *compute(a, b))
