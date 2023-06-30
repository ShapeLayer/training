from sys import stdin
input = stdin.readline

def compute(gets: str) -> int:
    if 'D' not in gets:
        return len(gets)
    return len(gets[:gets.index('D')])

if __name__ == '__main__':
    for _t in range(int(input())):
        gets = input().strip()
        print(compute(gets))
