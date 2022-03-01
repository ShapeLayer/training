gets = input()
stack = []
for s in gets:
    if s == '(':
        stack.append('(')
    elif s == ')':
        if stack:
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
        else:
            stack.append(')')
print(len(stack))