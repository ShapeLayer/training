from sys import stdin
while True:
    gets = stdin.readline().rstrip()
    if gets == '.':
        break
    flag = True
    stack = []
    for c in gets:
        if c in '([':
            stack += [c]
        elif c == ')':
            if not stack or stack[-1] != '(':
                flag = False
            else:
                stack.pop()
        elif c == ']':
            if not stack or stack[-1] != '[':
                flag = False
            else:
                stack.pop()
    if flag and not stack:
        print('yes')
    else:
        print('no')