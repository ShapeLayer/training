li = ['one', 'two', 'three', 'four']
li_1 = []
for content in li:
    li_1 += [content[0].upper() + content[1:]]
li_2 = list(map(lambda s: s[0].upper() + s[1:], li))
li_3 = [content[0].upper() + content[1:] for content in li]

if __name__ == '__main__':
    print(li_1)
    print(li_2)
    print(li_3)