from sys import stdin
input = stdin.readline

class Solve:
    def __init__(self, n: int, arr: list[int]):
        self.n = n
        self.arr = arr
        self.prefix_sum = [0]
        for i in range(n):
            self.prefix_sum.append(self.prefix_sum[i] + arr[i])

    def query(self, a: int, b: int) -> int:
        return self.prefix_sum[b] - self.prefix_sum[a - 1]

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    solve: Solve = Solve(n, arr)
    for each in [solve.query(*map(int, input().split())) for _i in range(m)]:
        print(each)
