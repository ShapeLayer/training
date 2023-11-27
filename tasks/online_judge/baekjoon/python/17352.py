from sys import stdin
input = stdin.readline

def compute(n: int, conn: list[list[int]]):
    parents: list[int] = [i for i in range(n + 1)]
    
    def find(n: int) -> int:
        if parents[n] == n:
            return n
        return find(parents[n])

    def merge(a: int, b: int):
        pa, pb = find(a), find(b)
        if pa < pb:
            parents[pb] = pa
            parents[b] = pa
        else:
            parents[pa] = pb
            parents[a] = pb

    for a, b in conn:
        merge(a, b)
    
    first, second = find(1), -1
    for i in range(2, n + 1):
        each = find(i)
        if each != first:
            second = each
            break
    return first, second

if __name__ == '__main__':
    n = int(input())
    conn = [[*map(int, input().split())] for _i in range(n - 2)]
    print(*compute(n, conn))
