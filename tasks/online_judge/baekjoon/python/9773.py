from sys import stdin
input = stdin.readline

def compute(id: str) -> str:
    val = sum([int(i) for i in id]) + int(id[10:]) * 10
    if val > 9999:
        return str(val % 10000).zfill(4)
    if val >= 1000:
        return str(val)
    return str(val + 1000)

if __name__ == '__main__':
    for i in range(int(input())):
        id = input().strip()
        print(compute(id))
