def compute(i: int, f: int) -> bool:
    return (i <= 1 and f <= 2) or (i <= 2 and f <= 1)

if __name__ == '__main__':
    for _t in range(int(input())):
        print('Yes' if compute(*map(int, input().split())) else 'No')
