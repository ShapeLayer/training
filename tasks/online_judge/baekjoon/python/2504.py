def compute(gets: str) -> int:
    stack = []
    res, cache = 0, 1
    prev = None
    for c in gets:
        if c == '(':
            stack.append('(')
            cache *= 2
        elif c == '[':
            stack.append('[')
            cache *= 3
        elif c == ')':
            if not stack or stack[-1] != '(':
                return 0
            if prev == '(':
                res += cache
            stack.pop()
            cache //= 2
        elif c == ']':
            if not stack or stack[-1] != '[':
                return 0
            if prev == '[':
                res += cache
            stack.pop()
            cache //= 3
        prev = c
    if stack:
        return 0
    return res

if __name__ == '__main__':
    print(compute(input()))
