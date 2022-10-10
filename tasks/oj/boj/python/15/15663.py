def proc(n: int, res: list, collected: list) -> None:
    '''
    collected는 현재 스텝에서 중복된 수열이 나오는 것을 방지
    prev는 한 스텝 이상 차이로 중복된 수열이 나오는 것을 방지
    ex 1)
    4 4 2
    2
    4
    4
    ex 2) 
    9 7 9 1
    9 1
    9 7
    9 9
    9 1
    9 7
    9 9
    '''
    if len(res) == m:
        print(*res)
        return
    prev = 0
    for i in range(n):
        if not collected[i] and prev != arr[i]:
            collected[i] = True
            res += [arr[i]]
            prev = arr[i]
            proc(n, res, collected)
            collected[i] = False
            res.pop()

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    proc(n, [], [False]*n)