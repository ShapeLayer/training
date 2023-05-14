INT_STR = [str(i) for i in range(10)] + [chr(65 + i) for i in range(26)]

def compute(n: int, b: int) -> str:
    result = []
    while n > 0:
        now = n % b
        n //= b
        result.append(INT_STR[now])
    return ''.join(result[::-1])

if __name__ == '__main__':
    n, b = map(int, input().split())
    print(compute(n, b))
