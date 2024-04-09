s = input()

def compute(s):
    if s[0] != '"':
        return False
    if s[-1] != '"':
        return False
    if s == '""' or s == '"':
        return False
    if not s:
        return False
    return True

print(s[1:-1] if compute(s) else 'CE')
