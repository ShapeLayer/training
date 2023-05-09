if __name__ == '__main__':
    n, m = 2, 1
    for i in range(int(input())):
        n += m
        m *= 2
    print(n**2)
