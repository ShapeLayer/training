if __name__ == '__main__':
    n, m = 100, 2
    start = [i for i in range(3, 100, 3)]
    end = []
    for i in range(1, 50):
        if i % 3 == 0:
            continue
        end.append(i)
    s = len(start)
    print(n, m, s)
    for i in range(s):
        print(start[i], end[i])
