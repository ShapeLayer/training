from sys import stdin
input = stdin.readline

parents: list = []

def merge(a: int, b: int):
    pa, pb = find(a), find(b)
    if pa < pb: parents[pb] = pa
    else: parents[pa] = pb
    
def find(n: int) -> int:
    if n == parents[n]: return n
    parents[n] = find(parents[n])
    return parents[n]

for testcase in range(1, int(input()) + 1):
    users: int = int(input())
    parents = [i for i in range(users)]
    relations: int = int(input())
    for _j in range(relations):
        a, b = map(int, input().split())
        merge(a, b)
    wants: int = int(input())
    print(f'Scenario {testcase}:')
    for _j in range(wants):
        a, b = map(int, input().split())
        if find(a) == find(b):
            print(1)
        else:
            print(0)
    print()
