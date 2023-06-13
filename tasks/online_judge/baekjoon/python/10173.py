from sys import stdin
input = stdin.readline

def compute(gets: str) -> bool:
    return 'nemo' in gets

if __name__ == '__main__':
    while True:
        gets = input().strip()
        if gets == 'EOI':
            break
        print('Found' if compute(gets.lower()) else 'Missing')
