def gen_fail_arr(n: int, arr: list[int]):
    fail = [0 for _i in range(n)]
    pre, post = 0, 1
    while post < n:
        if arr[pre] == arr[post]:
            pre += 1
            fail[post] = pre
            post += 1
        else:
            if pre != 0:
                pre = fail[pre - 1]
            else:
                fail[post] = 0
                post += 1
    return fail

def compute(n: int, arr: list[int]):
    fail = gen_fail_arr(n, arr)
    _max = max(fail)
    count = 0
    for each in fail:
        if each == _max:
            count += 1
    return _max, count

if __name__ == '__main__':
    n = int(input())
    arr = [*map(int, input().split())][::-1]
    _max, count = compute(n, arr)
    if _max != 0:
        print(_max, count)
    else:
        print(-1)
