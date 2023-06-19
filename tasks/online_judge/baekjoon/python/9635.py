from sys import stdin
input = stdin.readline

def compute(n: int, x: int, y: int, gets: list[int]) -> int:
    if gets[0] == x:
        if gets[-1] != y:
            return 1
        else:
            return 2
    if gets[-1] == y:
        return 3
    return 0

if __name__ == '__main__':
    table = ['OKAY', 'EASY', 'BOTH', 'HARD']
    for _t in range(int(input())):
        n, x, y = map(int, input().split())
        gets = list(map(int, input().split()))
        print(table[compute(n, x, y, gets)])
