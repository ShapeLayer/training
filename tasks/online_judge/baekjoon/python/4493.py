from sys import stdin
input = stdin.readline

def compute(n: int, game: list[list[str]]) -> int:
    result = 0
    for g in game:
        a, b = g
        if a == 'R':
            if b == 'S':
                result -= 1
            elif b == 'P':
                result += 1
        elif a == 'S':
            if b == 'R':
                result += 1
            elif b == 'P':
                result -= 1
        elif a == 'P':
            if b == 'R':
                result -= 1
            elif b == 'S':
                result += 1
    return result

if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        game: list[list[str]] = [input().strip().split() for _i in range(n)]
        result: int = compute(n, game)
        if result == 0:
            print('TIE')
        else:
            print('Player {}'.format(1 if result < 0 else 2))
