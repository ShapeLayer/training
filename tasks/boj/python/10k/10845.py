from sys import stdin

queue = []
for _ in range(int(stdin.readline())):
    command = stdin.readline().rstrip()
    if command.startswith('push'):
        queue += [int(command.split()[1])]
    elif command == 'pop':
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif command == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command == 'back':
        if queue:
            print(queue[len(queue)-1])
        else:
            print(-1)
