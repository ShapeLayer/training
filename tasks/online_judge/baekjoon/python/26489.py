from sys import stdin
input = stdin.readline

count = 0
while True:
    gets = None
    try:
        gets = input().strip()
    except EOFError:
        break
    if not gets:
        break
    count += 1

print(count)
