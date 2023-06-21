from collections import deque

def compute(n: int, l: int, arr: list[int]) -> list[int]:
    result = [arr[0]]
    queue: deque = deque([arr[0]])
    for i in range(1, n):
        queue.append(arr[i])
        result.append(result[-1])
        if i >= l:
            pop = queue.popleft()
            if pop == result[-2] or arr[i] < result[-2]:
                result[-1] = min(queue)
    return result

if __name__ == '__main__':
    n, l = map(int, input().split())
    arr = list(map(int, input().split()))
    print(*compute(n, l, arr))
