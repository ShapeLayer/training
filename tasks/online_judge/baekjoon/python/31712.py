(cu, du), (cd, dd), (cp, dp) = map(int, input().split()), map(int, input().split()), map(int, input().split())
h = int(input())

i = 0
while h > 0:
    if i % cu == 0:
        h -= du
    if i % cd == 0:
        h -= dd
    if i % cp == 0:
        h -= dp
    i += 1

print(i - 1)
