from sys import stdin
input = stdin.readline

def gcd(a, b):
    return gcd(b%a, a) if b % a else a

n = int(input())
trees = [0] * n
deltas = set()
for i in range(n):
    trees[i] = int(input())
trees.sort()
for i in range(1, n):
    deltas.add(trees[i] - trees[i-1])
deltas = list(deltas)[::-1]
while len(deltas) != 1:
    a, b = deltas.pop(), deltas.pop()
    new = gcd(a, b)
    if new not in deltas:
        deltas += [new]
print((trees[-1] - trees[0]) // deltas[0] - n + 1)
