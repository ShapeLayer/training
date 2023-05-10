from sys import stdin
input = stdin.readline

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        b_hp, b_mp, b_atk, b_def, a_hp, a_mp, a_atk, a_def = map(int, input().split())
        hp  = max(b_hp + a_hp, 1)
        mp  = max(b_mp + a_mp, 1)
        atk = max(b_atk + a_atk, 0)
        df  = b_def + a_def
        print(hp * 1 + mp * 5 + atk * 2 + df * 2)
