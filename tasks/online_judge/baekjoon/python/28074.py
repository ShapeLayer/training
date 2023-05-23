def compute(string: str) -> bool:
    chars = { c : False for c in 'MOBIS' }
    for char in string:
        if char in chars and not chars[char]:
            chars[char] = True
    return chars['M'] and chars['O'] and chars['B'] and chars['I'] and chars['S']

if __name__ == '__main__':
    print('YES' if compute(input()) else 'NO')
