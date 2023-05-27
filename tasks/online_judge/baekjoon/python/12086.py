from sys import stdin
input = stdin.readline

def compute(n: int, cards: list[str]) -> int:
    peek = cards[0]
    counts = 0
    for i in range(1, n):
        if peek > cards[i]:
            counts += 1
        else:
            peek = cards[i]
    return counts

if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        cards: list[str] = [input().strip() for _i in range(n)]
        result = compute(n, cards)
        print(f'Case #{t + 1}: {result}')
