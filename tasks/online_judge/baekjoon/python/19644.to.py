from sys import stdin
from collections import deque
input = stdin.readline

def compute(l, ml, mk, c, zombies):
    queue = [zombies.popleft() if len(zombies) else 0 for _i in range(ml)]
    while True:
        queue = [*map(lambda each: each - mk, queue)]

        if not queue:
            break

        if queue.pop(0) > 0:
            if c > 0:
                c -= 1
                continue
            return False
        if zombies:
            queue.append(zombies.popleft())
    return True

if __name__ == '__main__':
    l = int(input())
    ml, mk = map(int, input().split())
    c = int(input())
    zombies = deque([int(input()) for _i in range(l)])
    print('YES' if compute(l, ml, mk, c, zombies) else 'NO')
