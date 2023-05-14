def compute(a: int, b: int) -> str:
    result = [a // b]
    a = (a % b) * 10
    for _i in range(1050):
        result.append(a // b)
        a = (a % b) * 10
    return '{}.{}'.format(result[0], ''.join(map(str, result[1:])))

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(compute(a, b))
