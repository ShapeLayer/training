def compute(n: int, m: int) -> bool:
    return n * 100 >= m

if __name__ == '__main__':
    print('Yes' if compute(*map(int, input().split())) else 'No')
