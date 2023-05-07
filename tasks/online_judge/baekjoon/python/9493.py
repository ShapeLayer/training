from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    while True:
        m, a, b = map(int, input().split())
        if m == a == b == 0:
            break
        t = round((m / a - m / b) * 3600)
        s = t % 60
        m = (t % 3600) // 60
        h = t // 3600
        print('%d:%02d:%02d' % (h, m, s))
