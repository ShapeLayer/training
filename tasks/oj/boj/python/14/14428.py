from sys import stdin
input = stdin.readline

arr = []
tree = []

def query_result(lt, rt):
    if not lt: return rt
    if not rt: return lt
    res = (0, -1)
    if lt[0] > rt[0]:
        res = rt
    elif lt[0] < rt[0]:
        res = lt
    else:
        res = (lt[0], min(lt[1], rt[1]))
    return res

def init(start, end, index):
    if start == end:
        tree[index] = (arr[start], start+1)
        return tree[index]
    mid = (start + end) // 2
    lt = init(start, mid, index * 2)
    rt = init(mid + 1, end, index * 2 + 1)
    tree[index] = query_result(lt, rt)
    return tree[index]

def get_value(start, end, index, left, right):
    if left > end or right < start: return None
    if left <= start and right >= end: return tree[index]
    mid = (start + end) // 2
    return query_result(get_value(start, mid, index * 2, left, right), get_value(mid + 1, end, index * 2 + 1, left, right))

def update(start, end, index, target, delta):
    if target < start or target > end: return tree[index]
    if start == end:
        tree[index] = (tree[index][0] + delta, tree[index][1])
        return tree[index]
    mid = (start + end) // 2
    lt = update(start, mid, index * 2, target, delta)
    rt = update(mid + 1, end, index * 2 + 1, target, delta)
    tree[index] = query_result(lt, rt)
    return tree[index]


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    tree = [(0, -1)] * (n * 4)
    init(0, n-1, 1)
    for _i in range(int(input())):
        q, a, b = map(int, input().split())
        if q == 1:
            delta = -arr[a-1] + b
            update(1, n, 1, a, delta)
            print(arr, tree)
        elif q == 2:
            print(get_value(1, n, 1, a, b)[1])
