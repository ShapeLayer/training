from sys import stdin

deque = []

for _ in range(int(stdin.readline())):
    cmd = stdin.readline().rstrip()
    if cmd.startswith('push_front'):
        deque.insert(0, cmd.split()[1])
    elif cmd.startswith('push_back'):
        deque += [cmd.split()[1]]
    elif cmd == 'pop_front':
        if deque:
            print(deque.pop(0))
        else:
            print(-1)
    elif cmd == 'pop_back':
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif cmd == 'size':
        print(len(deque))
    elif cmd == 'empty':
        if deque:
            print(0)
        else:
            print(1)
    elif cmd == 'front':
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif cmd == 'back':
        if deque:
            print(deque[len(deque)-1])
        else:
            print(-1)
