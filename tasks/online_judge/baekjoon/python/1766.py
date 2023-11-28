from sys import stdin
import heapq
input = stdin.readline

def compute(n: int, favors: list[list[int]]) -> list[int]:
    conn: list[list[int]] = [[] for _i in range(n + 1)]
    priority: list[int] = [0 for _i in range(n + 1)]
    done: list[bool] = [False for _i in range(n + 1)]
    for first, second in favors:
        conn[first].append(second)
        priority[second] += 1
    
    res: list[int] = []
    queue: list[int] = []
    for i in range(1, n + 1):
        if priority[i] == 0 and not done[i]:
            heapq.heappush(queue, i)
            done[i] = True
        while queue:
            now = heapq.heappop(queue)
            res.append(now)
            for each in conn[now]:
                priority[each] -= 1
                if priority[each] == 0 and not done[each]:
                    heapq.heappush(queue, each)
                    done[each] = True
    return res

if __name__ == '__main__':
    n, m = map(int, input().split())
    favors: list[list[int]] = [[*map(int, input().split())] for _i in range(m)]
    print(*compute(n, favors))
