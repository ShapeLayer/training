if __name__ == '__main__':
    n = int(input())
    print('yes' if sum(map(int, input().split())) % 3 == 0 else 'no')
