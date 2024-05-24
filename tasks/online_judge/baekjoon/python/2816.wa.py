from sys import stdin
input = stdin.readline

def compute(kbs1, kbs2, channels):
    buf = ['1' * kbs1, '4' * kbs1, '1' * ((kbs2 + int(kbs1 > kbs2)) if kbs2 != 1 else 0), '4' * (kbs2 if kbs2 != 1 else 0)]
    return ''.join(buf)

if __name__ == '__main__':
    n = int(input())
    kbs1, kbs2 = -1, -1
    channels = []
    for i in range(n):
        gets = input().strip()
        if gets == 'KBS1':
            kbs1 = i
        elif gets == 'KBS2':
            kbs2 = i
        channels.append(gets)
    print(compute(kbs1, kbs2, gets))
