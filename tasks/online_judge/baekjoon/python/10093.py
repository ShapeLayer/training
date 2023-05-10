if __name__ == '__main__':
    s, e = map(int, input().split())
    if s > e:
        s, e = e, s
    arr = [i for i in range(s + 1, e)]
    print(len(arr))
    print(*arr)
