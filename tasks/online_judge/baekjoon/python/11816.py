def compute(n: str) -> int:
    if len(n) >= 3 and n[:2] == '0x':
        return int(n, 16)
    elif len(n) >= 2 and n[0] == '0':
        return int(n, 8)
    return int(n)

if __name__ == '__main__':
    print(compute(input()))
