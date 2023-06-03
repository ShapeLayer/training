def compute(k, w, m) -> int:
    result = 0
    while k < w:
        k += m
        result += 1
    return result

if __name__ == '__main__':
    print(compute(*map(int, input().split())))
