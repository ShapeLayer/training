while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break

    c = 0
    carried = 0
    while a > 0 or b > 0:
        ar, br = a % 10, b % 10

        c = int(ar + br + c >= 10)
        carried += c

        a, b = a // 10, b // 10
    print(carried)
