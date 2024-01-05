from sys import stdin
input = stdin.readline

gets = ''
while True:
    try:
        gets = input()
    except EOFError:
        break
    if not gets:
        break
    arr = list(map(int, gets.split()))
    print(arr[1] // (arr[0] + 1))
