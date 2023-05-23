def compute(n: int) -> list[int]:
    result = []
    l, r = 1, n
    prev_is_left = False
    while l <= r:
        if not prev_is_left:
            result.append(l)
            l += 1
        else:
            result.append(r)
            r -= 1
        prev_is_left = not prev_is_left
    return result

if __name__ == '__main__':
    n = int(input())
    print(*compute(n))
