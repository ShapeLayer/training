for _i in range(int(input())):
    pos, text = input().split()
    pos = int(pos)
    text = list(text)
    text.pop(pos-1)
    print(''.join(text))