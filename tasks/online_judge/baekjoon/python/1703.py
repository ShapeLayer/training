from sys import stdin
input = stdin.readline

def compute(tree: list[int]) -> int:
    leaf = 1
    for i in range(1, len(tree), 2):
        leaf = leaf * tree[i] - tree[i + 1]
    return leaf

if __name__ == '__main__':
    while True:
        tree = list(map(int, input().split()))
        if tree[0] == 0: break
        print(compute(tree))
