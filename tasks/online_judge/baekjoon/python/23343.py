x, y = input().split()
try:
    x, y = int(x), int(y)
except ValueError:
    print('NaN')
    exit()
print(x - y)
