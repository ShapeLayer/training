if __name__ == '__main__':
    n = int(input())
    if n % 2 == 1:
        l = n // 2
        print('*' * n)
        print(' ' * (n - l - 1) + '*')
        for i in range(l):
            print(' ' * (l - i - 1) + '*' + ' ' * (2 * i + 1) + '*')
    else:
        print("I LOVE CBNU")
