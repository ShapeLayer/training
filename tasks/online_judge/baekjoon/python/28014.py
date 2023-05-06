def compute(arr: list[int]) -> int:
    cnt, prev = 0, -1
    for t in arr:
        if prev <= t:
            cnt += 1
        prev = t
    return cnt

if __name__ == '__main__':
    n = int(input())
    print(compute(list(map(int, input().split()))))
