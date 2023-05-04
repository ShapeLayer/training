from sys import stdin
input = stdin.readline

class Conn:
    def __init__(self, a: int, b: int, cost: int):
        self.a = a
        self.b = b
        self.cost = cost

    def __eq__(self, other) -> bool:
        return self.cost == other.cost

    def __lt__(self, other) -> bool:
        return self.cost < other.cost

    def __le__(self, other) -> bool:
        return self < other or self == other

    def __repr__(self) -> str:
        return f'{self.a} <-> {self.b} // {self.cost}'

def compute(v: int, e: int, conns: list[Conn]):
    parents: list[int] = [i for i in range(v + 1)]

    def merge(a: int, b: int):
        pa, pb = find(a), find(b)
        if pa < pb:
            parents[pb] = pa
        else:
            parents[pa] = pb

    def find(n: int) -> int:
        if parents[n] == n:
            return n
        p = find(parents[n])
        parents[n] = p
        return p

    conns.sort()
    costs = 0
    for conn in conns:
        if find(conn.a) == find(conn.b):
            continue
        else:
            merge(conn.a, conn.b)
            costs += conn.cost
    return costs

if __name__ == '__main__':
    v = int(input())
    e = int(input())
    conns: list[Conn] = []
    for _i in range(e):
        a, b, c = map(int, input().split())
        conn: Conn = Conn(a, b, c)
        conns.append(conn)
    print(compute(v, e, conns))
