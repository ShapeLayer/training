from math import ceil

def compute(n: int, timeline: str) -> int:
    chicken = 0
    for each in timeline:
        if each == 'C':
            chicken += 1
    if chicken == n:
        return n
    healthy = n - chicken
    return ceil(chicken / (healthy + 1))

if __name__ == '__main__':
    n = int(input())
    timeline = input()
    print(compute(n, timeline))
