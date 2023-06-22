from sys import stdin
input = stdin.readline

def compute(target: str, content: list[str]) -> int:
    result = 0
    for char in (''.join(content)).lower():
        if char == target:
            result += 1
    return result

if __name__ == '__main__':
    while True:
        gets = input().split()
        if gets[0] == '#':
            break
        print(f'{gets[0]} {compute(gets[0], gets[1:])}')
