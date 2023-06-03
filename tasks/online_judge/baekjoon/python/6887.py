def compute(n: int) -> int:
    return int(n ** 0.5)

if __name__ == '__main__':
    print(f'The largest square has side length {compute(int(input()))}.')
