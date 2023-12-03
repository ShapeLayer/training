def compute(n: int, arr: list[int]) -> int:
    arr.sort()
    res = 0
    for i in range(n - 2):
        now = arr[i]
        if now > 0:
            break
        l, r = i + 1, n - 1
        while l < r:
            calced = now + arr[l] + arr[r]
            if calced < 0:
                l += 1
            elif calced > 0:
                r -= 1
            else:
                if arr[l] == arr[r]:
                    res += (r - l + 1) * (r - l) // 2
                    break
                else:
                    invoke_l, invoke_r = arr[l], arr[r]
                    counts_l, counts_r = 0, 0
                    while True:
                        if arr[l] != invoke_l:
                            break
                        else:
                            l += 1
                            counts_l += 1
                    while True:
                        if arr[r] != invoke_r:
                            break
                        else:
                            r -= 1
                            counts_r += 1
                    res += counts_l * counts_r
    return res

if __name__ == '__main__':
    n = int(input())
    arr = [*map(int, input().split())]
    print(compute(n, arr))
