def compute(n: int, t: int) -> int:
    arms = 0
    flag = False
    for _ in range(t):
        if arms == 2 * n:
            flag = True
        elif arms == 1:
            flag = False
        if flag > 0:
            arms -= 1
        else:
            arms += 1
    return arms

if __name__ == '__main__':
    n, t = map(int, input().split())
    print(compute(n, t))
