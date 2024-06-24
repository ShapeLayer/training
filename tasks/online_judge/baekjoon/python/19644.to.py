from sys import stdin
from collections import deque
input = stdin.readline

def compute(l, ml, mk, c, zombies):
    queue = deque([zombies.popleft() if len(zombies) else 0 for _i in range(ml)])
    while True:
        if not queue:
            break
        [queue.append(queue.popleft() - mk) for _i in range(min(ml, len(queue)))]

        if queue.popleft() > 0:
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
