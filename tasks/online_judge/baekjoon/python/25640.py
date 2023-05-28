from sys import stdin
input = stdin.readline

def compute(jinho: str, n: int, mbtis: list[str]) -> int:
    count = 0
    for mbti in mbtis:
        if jinho == mbti:
            count += 1
    return count

if __name__ == '__main__':
    jinho = input().strip()
    n = int(input())
    mbtis: list[str] = [input().strip() for _i in range(n)]
    print(compute(jinho, n, mbtis))
