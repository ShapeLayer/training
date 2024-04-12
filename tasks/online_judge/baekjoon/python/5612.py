from sys import stdin
input = stdin.readline

n = int(input())
car = int(input())
_max = car

for _i in range(n):
    _in, _out = map(int, input().split())
    car += _in - _out
    if car < 0:
        break
    _max = max(car, _max)

print(_max if car > 0 else 0)
