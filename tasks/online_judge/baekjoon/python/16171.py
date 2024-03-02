def filter(char):
    o = ord(char)
    if 97 <= o <= 122 or 65 <= o <= 90:
        return char
    return ''

gets = ''.join([*map(filter, input())])
print(int(input() in gets))
