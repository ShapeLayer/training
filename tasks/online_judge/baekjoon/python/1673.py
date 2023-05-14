from sys import stdin
input = stdin.readline

def compute(n: int, k: int) -> int:
    result = n
    while n // k:
        result += n // k
        n = n // k + n % k
    return result

if __name__ == '__main__':
    while True:
        gets = ''
        try:
            gets = input()
        except EOFError:
            break
        if not gets:
            break
        n, k = map(int, gets.split())
        print(compute(n, k))
