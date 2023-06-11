def compute(gets: str) -> str:
    def encryption(char: str) -> str:
        o: int = ord(char)
        if 97 <= o <= 122:
            return str(o - 96).zfill(2)
        if 65 <= o <= 90:
            return str(o - 38).zfill(2)
        if 48 <= o <= 57:
            return f'#{chr(o)}'
        return char
    buf = []
    for get in gets:
        buf.append(encryption(get))
    return ''.join(buf)
        
if __name__ == '__main__':
    print(compute(input()))
