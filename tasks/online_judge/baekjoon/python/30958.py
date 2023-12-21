from collections import Counter

if __name__ == '__main__':
    n = int(input())
    s = dict(Counter(input().replace(' ', '').replace(',', '').replace('.', '')))
    print(max(s.values()))
