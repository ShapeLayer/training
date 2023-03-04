from sys import stdin

stack = []
for _ in range(int(stdin.readline())):
    command = stdin.readline().rstrip()
    if command.startswith('push'):
        stack += [int(command.split()[1])]
    elif command == 'pop':
        if stack:
            l = len(stack)
            print(stack[l-1])
            stack.pop(l-1)
        else:
            print(-1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif command == 'top':
        if stack:
            print(stack[len(stack)-1])
        else:
            print(-1)
