from sys import stdin
input = stdin.readline

def compute(heads: int, opers: str) -> int:
    for oper in opers:
            if oper == 'c':
                heads += 1
            else:
                heads -= 1

            if heads == 0:
                return heads
    return heads

if __name__ == '__main__':
    k = int(input())
    for i in range(k):
        heads = int(input())
        opers = input().strip()
        result = compute(heads, opers)
        print(f'Data Set {i + 1}:')
        print(result)
        print()
