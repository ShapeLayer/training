INT_STR = [str(i) for i in range(10)] + [chr(65 + i) for i in range(26)]
STR_INT = { INT_STR[i] : i for i in range(len(INT_STR)) }

def compute(n: str, b: int) -> int:
    l = len(n)
    result = 0
    for i in range(l):
        result += STR_INT[n[l - i - 1]] * (b ** i)
    return result

if __name__ == '__main__':
    n, b = input().split()
    print(compute(n, int(b)))
