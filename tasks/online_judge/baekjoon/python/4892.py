def compute(n: int):
    n1 = 3 * n0
    n2 = n1 // 2 if n1 % 2 == 0 else (n1 + 1) // 2
    n3 = 3 * n2
    n4 = n3 // 9
    return n4, n0 == 2 * n4

if __name__ == '__main__':
    i = 0
    while True:
        i += 1
        n0 = int(input())
        if n0 == 0:
            break
        n4, is_even = compute(n0)
        print(f'{i}. even {n4}' if is_even else f'{i}. odd {n4}')
