var = input()
flags = 0
checks = ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '_']

def err():
    print('Error!')
    exit()

def cpptojava(var):
    new = ''
    upper_flag = False
    for c in var:
        if c == '_':
            # __가 연속해서 나오면 err
            if upper_flag: err()
            upper_flag = True
            continue
        if upper_flag:
            upper_flag = False
            new += c.upper()
        else:
            new += c
    return new

def javatocpp(var):
    new = ''
    for c in var:
        if ord('A') <= ord(c) <= ord('Z'): new += '_' + c.lower()
        else: new += c
    return new

# 맨 앞 문자가 _면 err
if var[0] == '_': err()
# 맨 앞 문자가 대문자면 err
if ord('A') <= ord(var[0]) <= ord('Z'): err()
# 맨 뒤 문자가 _면 err
if var[-1] == '_': err()

for c in var:
    for i in range(3):
        check = checks[i]
        if c in check:
            flags |= 1 << i

#             lower    upper    underdash
if   flags == 0 << 0 | 0 << 1 | 0 << 2: err()
elif flags == 1 << 0 | 0 << 1 | 0 << 2: print(var)
elif flags == 0 << 0 | 1 << 1 | 0 << 2: print(javatocpp(var))
elif flags == 0 << 0 | 0 << 1 | 1 << 2: err()
elif flags == 1 << 0 | 1 << 1 | 0 << 2: print(javatocpp(var))
elif flags == 1 << 0 | 0 << 1 | 1 << 2: print(cpptojava(var))
elif flags == 0 << 0 | 1 << 1 | 1 << 2: err()
elif flags == 1 << 0 | 1 << 1 | 1 << 2: err()