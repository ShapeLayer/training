from sys import stdin
gets = stdin.readline

arr = []
tree = []

def init(start, end, index):
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    mid = (start + end) // 2
    tree[index] = init(start, mid, index * 2) + init(mid + 1, end, index * 2 + 1)
    return tree[index]

def get_sums(start, end, index, left, right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree[index]
    mid = (start + end) // 2
    return get_sums(start, mid, index * 2, left, right) + get_sums(mid + 1, end, index * 2 + 1, left, right)

def update(start, end, index, target, delta):
    if target < start or target > end:
        return 
    tree[index] += delta
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, index * 2, target, delta)
    update(mid + 1, end, index * 2 + 1, target, delta)

if __name__ == '__main__':
    n, q = map(int, gets().split())
    arr = list(map(int, gets().split()))
    tree = [0 for _ in range(n*4)]
    init(0, n-1, 1)
    for _i in range(q):
        x, y, a, b = map(int, gets().split())
        print(get_sums(0, n-1, 1, x-1, y-1))
        delta = - arr[a-1] + b
        update(0, n-1, 1, a-1, delta)
