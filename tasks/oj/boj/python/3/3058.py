for _i in range(int(input())):
    evens = []
    for n in map(int, input().split()):
        if n % 2 == 0:
            evens += [n]
    print(sum(evens), min(evens))
