from sys import stdin
input = stdin.readline

def xor_from_1(n: int) -> int:
    '''
    1부터 N까지의 XOR 규칙: 4 단위로 아래 규칙이 반복됨
    https://www.geeksforgeeks.org/calculate-xor-1-n/
    '''
    mod = n % 4
    if mod == 0: return n
    elif mod == 1: return 1
    elif mod == 2: return n+1
    elif mod == 3: return 0

def proc(gets: iter) -> int:
    '''
    s부터 f까지의 XOR 규칙
    1부터 s-1, 1부터 f까지의 xor을 각각 구해서 서로 xor
    '''
    s, f = gets
    a = xor_from_1(s-1)
    b = xor_from_1(f)
    return a ^ b

if __name__ == '__main__':
    for _i in range(int(input())):
        print(proc(map(int, input().split())))
