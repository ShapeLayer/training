from sys import stdin
from collections import defaultdict
input = stdin.readline

if __name__ == '__main__':
    trees = defaultdict(int)
    gets = ''
    while True:
        try:
            gets = input().strip()
            if not gets:
                break
            trees[gets] += 1
        except EOFError:
            break
    total = sum(trees.values()) * 1000
    for k in sorted(trees.keys()):
        print('%s %.4f' % (k, ((trees[k] * 1000) / total) * 100))
