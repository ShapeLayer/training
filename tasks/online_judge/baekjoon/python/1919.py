if __name__ == '__main__':
    appeared = [0 for _i in range(26)]
    for o in (1, -1):
        for i in input().strip():
            appeared[ord(i) - 97] += 1 * o
    result = 0
    for i in appeared:
        result += abs(i)
    print(result)
