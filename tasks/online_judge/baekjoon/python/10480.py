from sys import stdin
input = stdin.readline

def compute(n: int) -> bool:
    return n % 2 == 0

if __name__ == '__main__':
    for _t in range(int(input())):
        n = int(input())
        is_even = compute(n)
        print(f'{n} is {"even" if is_even else "odd"}')
