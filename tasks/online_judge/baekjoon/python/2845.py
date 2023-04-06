l, p = map(int, input().split())
size = l*p
puts = list(map(int, input().split()))
print(' '.join(map(str, [put-size for put in puts])))