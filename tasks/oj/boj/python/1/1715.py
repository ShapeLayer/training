from sys import stdin
input = stdin.readline

arr = []
tree = []

def init(start, end, index):
    tree[index] = min(arr[start:end+1])
    if start == end: return
    mid = (start + end) // 2
    init(start, mid, index * 2)
    init(mid + 1, end, index * 2 + 1)

def query(start, end, index, left, right):
    if left > end or right < start:
        return (0, 0)
    if left <= start and right >= end:
        return (tree[index], (end - start + 1) * tree[index])
    mid = (start + end) // 2
    l_height, l_square = query(start, mid, index * 2, left, right)
    r_height, r_square = query(mid + 1, end, index * 2 + 1, left, right)
    f_height = min(l_height, r_height)
    print(f_height)
    f_square = f_height * (end - start + 1)
    return (min(tree[index], l_height, r_height), max(f_square, l_square, r_square))

n = int(input())
arr = [0 for _i in range(n)]
tree = [0 for _i in range(n * 4)]
for i in range(n):
    arr[i] = int(input())
init(0, n-1, 1)
print(tree)
for i in range(n):
    for j in range(n):
        print(i, j, query(0, n-1, 1, i+1, j+1))
