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
    n, m, k = map(int, gets().split())
    arr = [0 for _ in range(n)]
    tree = [0 for _ in range(n*4)]
    for i in range(n):
        arr[i] = int(gets())
    init(0, n-1, 1)
    for i in range(m+k):
        a, b, c = map(int, gets().split())
        b -= 1
        if a == 1:
            delta = c - arr[b]
            arr[b] = c
            update(0, n-1, 1, b, delta)
        elif a == 2:
            print(get_sums(0, n-1, 1, b, c-1))
