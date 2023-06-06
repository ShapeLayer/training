def compute(n: int, arr: list[int]) -> int:
    arr.sort()
    used: list[bool] = [False for _i in range(n)]

    def calculate(arr: list[int]) -> int:
        result = 0
        for i in range(n - 1):
            result += abs(arr[i] - arr[i + 1])
        return result

    def gen_new_arr(buf: list[int], result: int = -1) -> int:
        if len(buf) == n:
            return calculate(buf)
        for i in range(n):
            if not used[i]:
                used[i] = True
                req = gen_new_arr(buf + [arr[i]], result)
                used[i] = False
                if req > result:
                    result = req
        return result
    return gen_new_arr([])

if __name__ == '__main__':
    n = int(input())
    arr: list[int] = list(map(int, input().split()))
    print(compute(n, arr))
