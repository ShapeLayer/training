from random import randint
from collections import Counter

def gen() -> None:
    with open('randint30.txt', 'w', encoding='utf-8') as f:
        f.write(' '.join(list(map(str, [randint(1, 10) for _ in range(30)]))))

def load() -> None:
    cnt = Counter(map(int, open('randint30.txt', encoding='utf-8').read().split()))
    for i in range(1, 11):
        print('{} : {}개'.format(i, cnt[i] if i in cnt else 0))

if __name__ == '__main__':
    gen()
    load()