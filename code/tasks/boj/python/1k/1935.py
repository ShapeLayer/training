from sys import stdin
n = int(stdin.readline())
schm = stdin.readline().rstrip()
arr, stack = {}, []
for ord_n in range(65, 65 + n):
    arr[chr(ord_n)] = int(stdin.readline())
for s in schm:
    if ord(s) > 64 and ord(s) < 91:
        stack += [arr[s]]
    elif s == '+':
        stack += [stack.pop() + stack.pop()]
    elif s == '-':
        stack += [-1 * stack.pop() + stack.pop()]
    elif s == '*':
        stack += [stack.pop() * stack.pop()]
    elif s == '/':
        stack += [(stack.pop() / stack.pop())**-1]
print(format(stack[0], '.2f'))