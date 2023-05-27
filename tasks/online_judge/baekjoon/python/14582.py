def compute(u: list[int], s: list[int]) -> bool:
    us, ss = 0, 0
    result = False
    for i in range(9):
        us += u[i]
        if us > ss and us < ss + s[i]:
            result = True
        ss += s[i]
        if us > ss:
            result = False
    return result

if __name__ == '__main__':
    u, s = list(map(int, input().split())), list(map(int, input().split()))
    print('Yes' if compute(u, s) else 'No')
