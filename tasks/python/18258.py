import sys
n = int(sys.stdin.readline())
queue = []
s = 0

for i in range(n):
    cmd = sys.stdin.readline().rstrip()
    if cmd == 'pop':
        if len(queue) == s:
            print(-1)
        else:
            print(queue[s])
            s += 1
    elif cmd == 'size':
        print(len(queue)-s)
    elif cmd == 'empty':
        if len(queue) == s:
            print(1)
        else:
            print(0)
    elif cmd == 'front':
        if len(queue) == s:
            print(-1)
        else:
            print(queue[s])
    elif cmd == 'back':
        j = len(queue)
        if j == s:
            print(-1)
        else:
            print(queue[j-1])
    else:
        cmd = cmd.split()
        if cmd[0] == 'push':
            queue += [int(cmd[1])]