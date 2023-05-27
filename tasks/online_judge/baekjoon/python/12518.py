from sys import stdin
input = stdin.readline

def compute(name: str) -> str:
    if name[-1] == 'y':
        return 'nobody'
    if name[-1] in 'aeiou':
        return 'a queen'
    return 'a king'

if __name__ == '__main__':
    for t in range(int(input())):
        name = input().strip()
        print(f'Case #{t + 1}: {name} is ruled by {compute(name.lower())}.')
