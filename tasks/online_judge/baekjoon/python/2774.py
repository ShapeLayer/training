from sys import stdin
input = stdin.readline

def compute(n: int) -> int:
    exists = [False for _i in range(10)]
    
    while n > 0:
        ends: int = n % 10
        n //= 10
        exists[ends] = True

    count = 0
    for exist in exists:
        if exist:
            count += 1
    return count

if __name__ == '__main__':
    for t in range(int(input())):
        x = int(input())
        print(compute(x))
