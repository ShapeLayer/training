def compute(gets: str) -> str:
    each = []
    for get in gets:
        ord_calc = ord(get) - 3
        if 65 <= ord_calc <= 90:
            each.append(chr(ord_calc))
        else:
            each.append(chr(ord_calc + 26))
    return ''.join(each)

if __name__ == '__main__':
    print(compute(input()))
