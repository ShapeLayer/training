n = input()
if '7' in n:
    print(3 if int(n) % 7 == 0 else 2)
else:
    print(1 if int(n) % 7 == 0 else 0)
