def compute(s1: int, s2: int, s3: int) -> int:
    counts = {}
    for i in range(1, s1 + 1):
        for j in range(1, s2 + 1):
            for k in range(1, s3 + 1):
                sums = i + j + k
                if sums in counts:
                    counts[sums] += 1
                else:
                    counts[sums] = 1
    res, max_counts = -1, -1
    for key in counts:
        if counts[key] > max_counts:
            max_counts = counts[key]
            res = key
        elif counts[key] == max_counts:
            if res > key:
                res = key
    return res

if __name__ == '__main__':
    s1, s2, s3 = map(int, input().split())
    print(compute(s1, s2, s3))