from collections import Counter

if __name__ == '__main__':
    n = int(input())
    s = dict(Counter(input()))
    _max = max(s.values())
    buf = []
    for each in 'BSA':
        if not each in s:
            continue
        if s[each] == _max:
            buf.append(each)
    if len(buf) == 3:
        print('SCU')
    else:
        print(''.join(buf))
