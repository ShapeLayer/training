def compute(n: int) -> int:
    result = 0
    if n <= 198:
        for i in range(1, 100):
            for j in range(1, 100):
                if i + j == n:
                    result += 1
    return result

if __name__ == '__main__':
    n = int(input())
    print(compute(n))
