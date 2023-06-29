def compute(gets: str) -> int:
    left, right = 0, 0
    result = 0
    for i in range(len(gets) - 1):
        if gets[i] == gets[i + 1]:
            if gets[i] == '(':
                result += left * right
                right = 0
                left += 1
            else:
                right += 1
    result += left * right
    return result

if __name__ == '__main__':
    gets: str = input()
    print(compute(gets))
