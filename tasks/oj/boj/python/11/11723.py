from sys import stdin
gets = stdin.readline
arr = [0 for _i in range(21)]
for _i in range(int(gets())):
    command = gets().split()
    if command[0] == 'add':
        n = int(command[1])
        arr[n] = 1
    elif command[0] == 'remove':
        n = int(command[1])
        arr[n] = 0
    elif command[0] == 'check':
        n = int(command[1])
        if arr[n] == 1:
            print(1)
        else:
            print(0)
    elif command[0] == 'toggle':
        n = int(command[1])
        arr[n] += 1
        arr[n] %= 2
    elif command[0] == 'all':
        arr = [1 for _i in range(21)]
    elif command[0] == 'empty':
        arr = [0 for _i in range(21)]