keyboard = '`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;\'ZXCVBNM,./'
while True:
    gets = []
    try:
        gets = list(input())
    except EOFError:
        break
    if not gets: break
    for i in range(len(gets)):
        if gets[i] not in keyboard: continue
        gets[i] = keyboard[keyboard.index(gets[i])-1]
    print(''.join(gets))