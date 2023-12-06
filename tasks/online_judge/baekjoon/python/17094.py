from collections import Counter

if __name__ == '__main__':
    ln = int(input())
    _d = dict(Counter(input()))
    if '2' not in _d: _d['2'] = 0
    if 'e' not in _d: _d['e'] = 0
    print('2' if _d['2'] > _d['e'] else 'e' if _d['2'] < _d['e'] else 'yee')
