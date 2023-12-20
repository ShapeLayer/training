def compute(n: int):
    line = [0 for _i in range(n)]
    res = 0

    def _check(each: int) -> bool:
        for i in range(each):
            if line[each] == line[i]:
                return False
            if abs(line[each] - line[i]) == each - i:
                return False
        return True

    def step(each: int):
        nonlocal res
        if each == n:
            res = res + 1
        else:
            for i in range(n):
                line[each] = i
                if _check(each):
                    step(each + 1)
    
    step(0)
    return res

if __name__ == '__main__':
    print(compute(int(input())))
