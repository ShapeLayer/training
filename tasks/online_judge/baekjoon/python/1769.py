gets = input()
n = 0
counts = 0
for s in gets:
    n += int(s)
counts += 1
while n >= 10:
    new = 0
    while n != 0:
        new += n % 10
        n /= 10
    n = new
    counts += 1
print(counts)
print('YES' if n == 3 or n == 6 or n == 9 else 'NO')