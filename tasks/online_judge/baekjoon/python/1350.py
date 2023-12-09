from math import ceil

def compute(n: int, files: list[int], cluster: int):
    uses = 0
    for each in files:
        uses += ceil(each / cluster)
    return uses * cluster

if __name__ == '__main__':
    n = int(input())
    files = [*map(int, input().split())]
    cluster = int(input())
    print(compute(n, files, cluster))
