from sys import stdin, setrecursionlimit
from collections import defaultdict
setrecursionlimit(int(1e7))
input = stdin.readline

def compute(n: int, m: int, conn_fw: list[list[int]], conn_rw: list[list[int]], costs: list[list[int]], src: int, dest: int) -> tuple[int]:
    costs_max: list[int] = [0 for _i in range(n + 1)]
    
    def evaluate_cost():
        visits: list[bool] = [False for _i in range(n + 1)]
        def _dfs(_from: int, node: int):
            if visits[node]:
                return
            costs_max[node] = max(costs_max[node], costs_max[_from] + costs[_from][node])
            if node == dest:
                return
            for each in conn_fw[node]:
                visits[node] = True
                _dfs(node, each)
                visits[node] = False
        visits[0] = True
        _dfs(0, src)
        return costs_max[dest]
    
    def trace_expensive_path():
        exp_count = 0
        visits: list[bool] = [False for _i in range(n + 1)]
        def _dfs(_from: int, node: int):
            nonlocal exp_count
            if costs_max[_from] == costs_max[node] + costs[node][_from]:
                if _from != 0:
                    exp_count += 1
                if node == src:
                    return
                for each in conn_rw[node]:
                    visits[node] = True
                    _dfs(node, each)
                    visits[node] = False
            return
        visits[0] = True
        costs_max[0] = costs_max[dest]
        _dfs(0, dest)
        return exp_count

    exp_cost = evaluate_cost()
    exp_count = trace_expensive_path()
    return exp_cost, exp_count

if __name__ == '__main__':
    n, m = int(input()), int(input())
    conn_fw, conn_rw = defaultdict(list), defaultdict(list)
    costs = defaultdict(lambda: defaultdict(int))
    for _i in range(m):
        _from, _to, cost = map(int, input().split())
        conn_fw[_from].append(_to)
        conn_rw[_to].append(_from)
        costs[_from][_to] = cost
    src, dest = map(int, input().split())
    cost, count = compute(n, m, conn_fw, conn_rw, costs, src, dest)
    print(cost)
    print(count)
