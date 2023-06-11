from sys import stdin
input = stdin.readline

def compute(s: int, gets: list[int]) -> int:
    cnt = 0
    for get in gets:
        if s in get:
            cnt += 1
    return cnt

if __name__ == '__main__':
    s = input().strip()
    gets = []
    while True:
        get = ''
        try:
            get = input()
        except EOFError:
            break
        get = get.strip()
        if not get:
            break
        gets.append(get)
    print(compute(s, gets))
