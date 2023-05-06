from sys import stdin
input = stdin.readline

def compute(starts: list[int], ends: list[int]) -> list[int]:
    dp: list[int] = [0 for _i in range(1000001)]
    start = starts.pop()
    end = ends.pop()
    for t in range(1, 1000001):
        dp[t] = dp[t - 1]
        while t == start:
            dp[t] += 1
            if starts:
                start = starts.pop()
            else:
                start = 1e10
        while t == end + 1:
            dp[t] -= 1
            if ends:
                end = ends.pop()
            else:
                end = 1e10
    return dp

if __name__ == '__main__':
    n = int(input())
    starts: list[int] = []
    ends: list[int] = []
    for _i in range(n):
        s, e = map(int, input().split())
        starts.append(s)
        ends.append(e)
    starts.sort(reverse=True)
    ends.sort(reverse=True)
    timeline: list[int] = compute(starts, ends)
    q = int(input())
    for qt in map(int, input().split()):
        print(timeline[qt])
