from sys import stdin
input = stdin.readline

def compute(opers: list[tuple[int]]) -> list[int]:
    cards = [i for i in range(21)]
    for oper in opers:
        s, e = oper
        e += 1
        cards[s:e] = cards[s:e][::-1]
    return cards

if __name__ == '__main__':
    opers = [tuple(map(int, input().split())) for _i in range(10)]
    print(*compute(opers)[1:])
