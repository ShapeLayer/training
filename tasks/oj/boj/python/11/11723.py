from sys import stdin
gets = stdin.readline
arr = []
for _i in range(int(gets())):
    command = gets().split()
    if command[0] == 'add':
        n = int(command[1])
        if n not in arr:
            arr += [n]
    elif command[0] == 'remove':
        n = int(command[1])
        if n in arr:
            arr.remove(n)
    elif command[0] == 'check':
        n = int(command[1])
        if n in arr:
            print(1)
        else:
            print(0)
    elif command[0] == 'toggle':
        n = int(command[1])
        if n in arr:
            arr.remove(n)
        else:
            arr += [n]
    elif command[0] == 'all':
        arr = [i for i in range(1, 21)]
    elif command[0] == 'empty':
        arr = []