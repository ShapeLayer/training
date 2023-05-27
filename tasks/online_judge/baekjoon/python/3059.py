from sys import stdin
input = stdin.readline

def compute(gets: str) -> int:
    exists = { chr(i) : False for i in range(65, 91) }
    for get in gets:
        exists[get] = True
    result = 0
    for exist in exists:
        if not exists[exist]:
            result += ord(exist)
    return result

if __name__ == '__main__':
    for t in range(int(input())):
        print(compute(input().strip()))
