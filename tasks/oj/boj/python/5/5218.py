for _i in range(int(input())):
    a_body, b_body = input().split()
    score = []
    for i in range(len(a_body)):
        a = a_body[i]
        b = b_body[i]
        res = ord(b) - ord(a)
        if res < 0: res = ord(b) + 26 - ord(a)
        score += [res]
    print(f'Distances: {" ".join(map(str, score))}')
