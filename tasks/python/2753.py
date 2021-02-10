def clear(a, b):
    return a%b == 0

year = int(input())
if clear(year, 4) and not clear(year, 100):
    print(1)
elif clear(year, 400):
    print(1)
else:
    print(0)