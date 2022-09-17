from sys import stdin
input = stdin.readline
DIV = 1000000007

arr = []
tree = []

def init(start, end, index):
    if start == end:
        tree[index] = arr[start]
        return tree[index]
    mid = (start + end) // 2
    tree[index] = (init(start, mid, index * 2) * init(mid + 1, end, index * 2 + 1)) % DIV
    return tree[index]

def get_sums(start, end, index, left, right):
    if left > end or right < start:
        return 1
    if left <= start and right >= end:
        return tree[index]
    mid = (start + end) // 2
    return (get_sums(start, mid, index * 2, left, right) * get_sums(mid + 1, end, index * 2 + 1, left, right)) % DIV

def update(start, end, index, target, new):
    if target < start or target > end:
        return 
    if start == end:
        tree[index] = new
        return
    if arr[target] == 0:
        tree[index] == new
    else:
        tree[index] = tree[index] * new // arr[target]
    mid = (start + end) // 2
    update(start, mid, index * 2, target, new)
    update(mid + 1, end, index * 2 + 1, target, new)
    tree[index] = (tree[index * 2] * tree[index * 2 + 1]) % DIV

n, m, k = map(int, input().split())
arr = [1 for _ in range(n)]
tree = [1 for _ in range(n*4)]
for i in range(n):
    arr[i] = int(input())
init(0, n-1, 1)
for _q in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(0, n-1, 1, b-1, c)
        arr[b-1] = c
    elif a == 2: print(get_sums(0, n-1, 1, b-1, c-1))
